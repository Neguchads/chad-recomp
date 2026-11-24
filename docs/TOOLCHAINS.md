# Toolchain survey

Snapshot: 2026-11-24. References are not dependencies or endorsements. Research status is conservative; verify upstream revision, license and actual game coverage before use.

| Tool | Role |
|---|---|
| [N64Recomp](https://github.com/N64Recomp/N64Recomp) | AOT CPU; symbols, config, patches; pair with runtime |
| [N64ModernRuntime](https://github.com/N64Recomp/N64ModernRuntime) | shared runtime |
| [RT64](https://github.com/rt64/rt64) | renderer |
| [XenonRecomp](https://github.com/hedge-dev/XenonRecomp) | PPC AOT; runtime separate |
| [XenosRecomp](https://github.com/hedge-dev/XenosRecomp) | shader translation |
| [ReXGlue](https://github.com/rexglue/rexglue-sdk) | integrated Xbox 360 SDK; runtime lineage from Xenia |
| [PS2Recomp](https://github.com/ran-j/PS2Recomp) | EE translation and runtime |
| [ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp) | PS2 native and WebAssembly research |
| [ps3recomp](https://github.com/sp00nznet/ps3recomp) | PPU and services; SPU/RSX coverage is project-specific |
| [psprecomp](https://github.com/sp00nznet/psprecomp) | Allegrex to C and runtime |
| [PSXRecomp](https://github.com/RetroPortingToolKit/psxrecomp) | PS1 framework |
| [RecompOne](https://github.com/BlackLabelHQ/RecompOne) | PS1 C# translation; research |
| [gbarecomp](https://github.com/sp00nznet/gbarecomp) | ARM/Thumb AOT, conformance harness |
| [gbarecomp (alternative)](https://github.com/mstan/gbarecomp) | GBA ecosystem |
| [ndsrecomp](https://github.com/RetroPortingToolKit/ndsrecomp) | early NDS research |
| [ndskit / wiikit](https://github.com/vs-sr-dev) | console-specific kits; inspect each project |
| [saturnkit](https://github.com/vs-sr-dev/saturnkit) | SH-2 and hardware runtime research |
| [SaturnRecomp](https://github.com/sonsegajp/SaturnRecomp) | interpreter-first research; not proof of AOT |
| [dcrecomp](https://github.com/sp00nznet/dcrecomp) | SH-4 to C |
| [DolRecomp](https://github.com/ExpansionPak/DolRecomp) | CPU lifting; runtime separate |
| [Wiicompiled](https://github.com/patchzyy/Wiicompiled) | DOL/REL and runtime |
| [snesrecomp](https://github.com/RetroPortingToolKit/snesrecomp) | SNES research |
| [TotK Recomp](https://github.com/valentderah/totk-pc-recomp) | per-game AArch64 pipeline and runtime |
| [nxrecomp](https://github.com/drakolordx7/nxrecomp) | Switch research, differential instruction tests |
| [SwitchRecomp](https://github.com/kaiyao7/SwitchRecomp) | early Switch framework, no general game compatibility |
| [XboxXBERecomp](https://github.com/TGP482/XboxXBERecomp) | original Xbox research |
| [pcrecomp](https://github.com/sp00nznet/pcrecomp) | legacy PC executable analysis and runtime |
| [neogeorecomp](https://github.com/sp00nznet/neogeorecomp) | 68000 translation and board runtime |
| [smsggrecomp](https://github.com/mstan/smsggrecomp) | Z80 console research |
| [vbrecomp](https://github.com/mstan/vbrecomp) | V810 translation and fallback |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | analysis and decompilation |
| [RecompLauncher](https://github.com/elripalda/RecompLauncher) | external distribution adapter |
| [Recompendium](https://recompendium.com/en/launchers/) | secondary tool catalogue |
| [recomp.board](https://recomp.fyi/toolchains) | secondary toolchain catalogue |

## Selection
Check ISA, ABI, executable/container, coverage of graphics/audio/kernel, deterministic output, license and evidence. Do not select by stars alone. Compare candidates using the same legal homebrew fixture, record missing opcodes/services and benchmark on identical hardware.
