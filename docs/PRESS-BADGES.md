# RecompLauncher and RecompStore press badges

Optional documentation convention for eligible projects. This does not confer developer verification, platform support or store approval.

- Use the official [RecompLauncher press kit](https://recomplauncher.com/press) and [RecompStore press kit](https://recompstore.com/press). Keep SVG artwork intact; never recolor, stretch, crop or redraw it. Preserve spacing and intrinsic proportions.
- Use the appropriate light or dark variant for the background. Use the officially supplied fallback when an alternative is not verified.
- Add the launcher badge only after confirming the actual public game listing and repository. Link the specific game page, not the store homepage. Use RecompLauncher for PC; use RecompStore for applicable PS5 listings.
- Add a verified developer badge only if the actual maintainer holds that verification; link their verified profile. It is not a game certification or endorsement.
- Preserve license, supported-platform, experimental-status and input disclosures. Do not imply a ready-to-play release for source-only previews.
- Group official badges near the top of the README, separate from CI, platform, language and release badges. Mirror them in localized READMEs where present.

## Example

Replace placeholders with confirmed listing and developer URLs before publishing.

```html
<p align="center">
  <a href="https://recomplauncher.com/game/CONFIRMED_GAME_SLUG">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://recomplauncher.com/assets/press/launcher/badge-light.svg">
      <img src="https://recomplauncher.com/assets/press/launcher/badge-dark.svg" alt="Get it on RecompLauncher" height="48">
    </picture>
  </a>
  <a href="https://recompstore.com/dev/VERIFIED_DEVELOPER">
    <img src="https://recompstore.com/assets/press/verified-dark.svg" alt="Verified developer on RecompStore" height="48">
  </a>
</p>
```

Confirm the destinations and asset availability, inspect both GitHub themes, and retain actual project support status.

Official [RecompLauncher press-kit ZIP](https://recomplauncher.com/assets/press/launcher/recomplauncher-press-kit.zip) (external reference; not redistributed by CSR).
