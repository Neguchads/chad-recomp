# Optional NAVI AutoVerify for Recomp releases

NAVI Core provides an experimental reusable public VirusTotal hash report
workflow in [NAVI Core PR #36](https://github.com/Neguchads/navi-core/pull/36).
It is not an approved release gate yet.

## Pilot adoption

Pilot on CDOS Nintendo DS Recomp, then reuse for CSOTN Saturn Recomp, CCOD Xbox
Recomp and other authorized public non-commercial projects.

1. Build and test the release artifact using the project-native pipeline.
2. Record SHA-256 and verify provenance independently.
3. Upload the exact public release executable as a named GitHub Actions artifact
   in the same trusted workflow run; do not include ROMs, BIOS, credentials or
   unapproved third-party assets.
4. After approving the Core revision, copy the illustrative job below to the
   release workflow and set the secret VT_API_KEY in GitHub.
5. Check the output report and review any detections; never declare a binary safe
   solely because no engines detected it.
6. For unknown hashes, manually submit an authorized file only after reviewing
   VirusTotal disclosure terms, then re-run the lookup later. No automated upload.
7. Require independent local security checks; a failed or missing report must not
   be reported as clean. Do not automate release publication until the pilot passes.

## Example job (not active)

```yaml
  autoverify:
    needs: [build]
    permissions:
      contents: read
      actions: read
    uses: Neguchads/navi-core/.github/workflows/autoverify.yml@REVIEWED_CORE_SHA
    with:
      core_sha: REVIEWED_CORE_SHA
      artifact_name: windows-release
      filename: game.exe
      approved_public_noncommercial: true
    secrets:
      VT_API_KEY: ${{ secrets.VT_API_KEY }}
```

Replace the placeholder with the same reviewed 40-character commit hash in both
positions; replace build/job and file names with the actual pipeline values.
Use only on trusted public main/tag push or manual dispatch. The free public API
is restricted to non-commercial use and limited to 4 requests/minute and 500/day
across the account. Serialize queries across projects and stop on quota errors.
No secrets should be inherited wholesale; no paid services are authorized.
A trusted caller must check non-skipped success if a report is required.

References: [public API constraints](https://docs.virustotal.com/reference/public-vs-premium-api)
and [file report](https://docs.virustotal.com/reference/file-info).
