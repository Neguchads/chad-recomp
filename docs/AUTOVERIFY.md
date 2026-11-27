# Optional NAVI AutoVerify for Recomp releases

NAVI Core provides an experimental reusable public VirusTotal hash report
workflow in [NAVI Core PR #36](https://github.com/Neguchads/navi-core/pull/36).
It is not an approved release gate yet.

## Pilot adoption

Only stable final public delivery artifacts (vX.Y.Z) of CDOS Nintendo DS Recomp,
CSOTN Saturn Recomp and CCOD Xbox Recomp are eligible. Never run against normal
pushes, pull requests, nightly, beta, RC or intermediate builds. Other projects
require an explicit reviewed allowlist extension.

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

## Pre-publication final build example (not active)

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
      expected_sha256: ${{ needs.build.outputs.release_sha256 }}
      final_delivery: true
      approved_public_noncommercial: true
    secrets:
      VT_API_KEY: ${{ secrets.VT_API_KEY }}
```

Replace the placeholder with the same reviewed 40-character commit hash in both
positions; replace build/job and file names with the actual pipeline values.
Use only on trusted stable tag push or manual dispatch on that tag, with the
build job producing the final artifact and a verified release_sha256 output. The free public API
is restricted to non-commercial use and limited to 4 requests/minute and 500/day
across the account. Serialize queries across projects and stop on quota errors.
No secrets should be inherited wholesale; no paid services are authorized.
A trusted caller must check non-skipped success if a report is required.

References: [public API constraints](https://docs.virustotal.com/reference/public-vs-premium-api)
and [file report](https://docs.virustotal.com/reference/file-info).

## Published release check

Use the shared `autoverify-published.yml` workflow from a `release: published`
caller only for a stable published release with a configured exact asset name
(or `{tag}` filename template). The project wrappers are in CDOS PR #59,
CSOTN PR #19 and CCOD PR #16. Set `NAVI_RELEASE_ASSET` to enable automatic
integrity verification and `NAVI_AUTOVERIFY_ENABLED=true` with `VT_API_KEY`
only if authorized non-commercial external lookup is wanted. Manual verification
of existing stable releases requires an independent expected hash. Do not query
both before and after publication automatically. Neither workflow publishes or
uploads files to VirusTotal. The current Core pin is
`c6037185830f24770f856d4cd69791c686095bc5`, pending latest CI and review.
