# Platform profiles

`demonstrated` = a credible title-specific demonstration exists, not a general compatibility guarantee. `research` = candidate tool or approach; `unverified` = no generic toolchain confirmed in this survey. Emulator names identify possible reference implementations only; verify exact revision and license.

| Platform | CPU | Candidate | Evidence | Critical gaps | Reference |
|---|---|---|---|---|---|
| NES / Famicom | 6502 derivative | NESRecomp (catalogued) | research | Mapper, PPU, timing, APU | Mesen |
| SNES / Super Famicom | 65C816 + SPC700 | snesrecomp; game-specific decomp | research | PPU, APU, coprocessors, bank mapping | bsnes / Mesen |
| Nintendo 64 | MIPS VR4300 + RSP | N64Recomp + N64ModernRuntime + RT64 | demonstrated | RSP, microcode, overlays, RDP, timing | mupen64plus / ares |
| GameCube | PowerPC Gekko | DolRecomp / Wiicompiled; decomp-toolkit | research | GX, DSP, OS, REL modules | Dolphin |
| Wii | PowerPC Broadway | Wiicompiled / DolRecomp / wiikit | research | IOS, GX, DSP, motion input, REL | Dolphin |
| Wii U | PowerPC Espresso | DolRecomp experimental; per-game routes | research | GX2, OS, multicore, shaders | Cemu |
| Nintendo Switch | AArch64 | TotK pipeline / nxrecomp / SwitchRecomp | demonstrated | Horizon IPC, NVN, shader translation, NSO relocation | Ryujinx (historical reference) |
| Nintendo Switch 2 | AArch64 | Per-game research; no general SDK verified | unverified | OS, graphics, memory, ABI | Not verified |
| Game Boy | SM83 | gb-recompiled (catalogued) | research | MBC, LCD, timers, APU | SameBoy |
| Game Boy Color | SM83 | gb-recompiled (catalogued) | research | Banking, color, speed modes | SameBoy |
| Game Boy Advance | ARM7TDMI ARM/Thumb | gbarecomp (sp00nznet and mstan) | research | DMA, IRQ, BIOS services, PPU, audio | mGBA |
| Nintendo DS / DSi | ARM9 + ARM7 | ndsrecomp / ndskit | research | Dual CPU, overlays, IPC, 2D/3D, touch | melonDS |
| Nintendo 3DS | ARM11 + ARM9 | 3dsrecomp (catalogued) | research | PICA200, service IPC, dual-screen, DSP | Citra (historical reference) |
| Virtual Boy | NEC V810 | vbrecomp | research | VIP, VSU, interrupts, stereo display | Mednafen |
| PlayStation | MIPS R3000A | PSXRecomp / RecompOne / PSXPort | research | GTE, GPU, CD, SPU, overlays, BIOS calls | DuckStation |
| PlayStation 2 | MIPS R5900 + IOP + VU0/VU1 | PS2Recomp / ps2-web-recomp | demonstrated | VU microprograms, GS, DMA, IOP, SPU2, FPU semantics | PCSX2 |
| PlayStation 3 | Cell PPE + SPUs | ps3recomp | research | SPU, PPU ABI, RSX, syscalls, threads | RPCS3 |
| PlayStation 4 | x86-64 | bbport / game-specific native runtime | research | Orbis ABI, GPU command streams, OS APIs | shadPS4 |
| PlayStation 5 | x86-64 | Per-game research; no general SDK verified | unverified | Platform ABI, GPU, system services | Not verified |
| PSP | MIPS Allegrex | psprecomp | research | VFPU, GE, kernel, threading, imports | PPSSPP |
| PS Vita | ARM Cortex-A9 | Game-specific research; no general SDK verified | unverified | GXM, imports, OS, NEON | Vita3K |
| Xbox | x86 | XboxXBERecomp / XboxRecomp (catalogued) | research | XBE loader, kernel exports, NV2A, x86 ABI | xemu / Cxbx-Reloaded |
| Xbox 360 | PowerPC Xenon | XenonRecomp + XenosRecomp / ReXGlue | demonstrated | VMX128, XEX, Xenos, kernel, endian, atomics | Xenia |
| Xbox One | x86-64 | No general SDK verified | unverified | System ABI, sandbox, graphics, services | Not verified |
| Xbox Series | x86-64 | No general SDK verified | unverified | System ABI, graphics, services | Not verified |
| Master System / Game Gear | Z80 | smsggrecomp | research | VDP, PSG, mapper, timing | Gearsystem |
| Mega Drive / Genesis / Sega CD | 68000 + Z80; Sega CD extra CPU | SegaGenesisRecomp (catalogued) | research | VDP, audio, bank switching; CD timing | Genesis Plus GX |
| Sega 32X | 68000 + dual SH-2 + Z80 | Per-game research; no general SDK verified | unverified | Multi-CPU synchronization, framebuffer, audio | ares |
| Sega Saturn | Dual SH-2 + 68000 | saturnkit / SaturnRecomp | research | VDP1/2, SCU/DSP, SCSP, CD, dual CPU | Mednafen / Kronos |
| Dreamcast / NAOMI | SH-4 + ARM7 sound CPU | dcrecomp / KatanaRecomp | research | PowerVR, GD-ROM, Maple, AICA, MMU | Flycast |
| Neo Geo AES/MVS | 68000 + Z80 | neogeorecomp | research | Sprite hardware, banks, BIOS services, sound | MAME / FBNeo |
| Arcade (multiple boards) | Board-specific | Per-board adapters; no universal CPU or runtime | unverified | Board, firmware, protection, timing, peripherals | MAME |
| PC Engine / TurboGrafx-16 | HuC6280 | Per-game research | unverified | VDC, audio, bank mapping, CD expansion | Mednafen |
| Atari 2600 | 6507 | Per-game research | unverified | TIA cycle timing, RIOT, banks | Stella |
| Atari Lynx | 65SC02 | lynxrecomp (family reference) | research | Mikey, Suzy, timing | Mednafen |
| Atari Jaguar | 68000 + GPU/DSP | Per-game research | unverified | RISC coprocessors, object processor | BigPEmu (reference only) |
| 3DO | ARM60 | Per-game research | unverified | CEL rendering, DSP, OS services | Opera |
| CD-i | 68000 family | Per-game research | unverified | OS-9, video, input | MAME |
| PC DOS | x86 | pcrecomp | research | Real/protected mode, DOS interrupts, VGA, audio | DOSBox-X |
| Legacy Windows | x86 / x86-64 | pcrecomp / recomp-kit; API compatibility | research | PE imports, Win32, DirectX, ABI | Wine (compatibility layer) |
| Other / custom platform | Project-defined | Custom adapter | unverified | Document CPU, ABI, firmware and peripherals | Project-defined |

## Universal extension
Create a new profile for each distinct hardware revision or arcade board if its ABI or timing differs. Never infer compatibility from ISA alone.
