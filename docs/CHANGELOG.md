# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-03-15
### Added
- **Global Commands:** Now you can run the tool from anywhere using `sstatus` (monitor) and `sstatus-db` (database manager).
- **Multi-Language (i18n):** Full support for English and Spanish across all CLI modules using a dedicated `i18n.py` engine and `config.json`.
- **New Uninstaller:** Added `uninstall.sh` to safely remove the app, environment, and optionally user data.

### Changed
- **Installation Overhaul:** `setup.sh` now features an interactive language selector and creates a dedicated virtual environment in `~/.server_status_cli_app` with shims in `~/.local/bin`.
- **Database Manager:** Updated `db.py` to v1.2 with multi-language support.

### Upgrades
- **README:** Updated the README file with the new flags, crosslink and new features.


## [1.2.0] - 2026-01-28
### Added
- **HTML Reports:** Added the ability to generate professional, dark-themed HTML reports of the check results using the `-r` or `--report` flag.

## [1.1.0] - 2026-01-25
### Added
- **Enhanced Docs:** Profesional documentation with installation instructions, usage examples, and a detailed description of the code, multilanguage support, and Changelog for future updates.
- **Quick execution:** Quickly check the status of multiple sites by running the script with the `-f` or `--fast` flag.

## [1.0.0] - 2025-12-01
### Added
- Initial release.
- Persistent JSON management as a database (clients information).
- Real-time monitoring.
- TUI dashboard.
- Alerts and notifications.
