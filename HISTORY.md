# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.63.18] - 2020-11-03

### Added

- Added a generic driver for reporting results for non-UI tests to TestProject

### Fixed

- Fixed issue with the `packaging` dependency package not being installed when installing the SDK

## [0.63.15] - 2020-09-17

### Added

- Automatically capture a screenshot whenever a WebDriver command fails
- Add `@report_assertion_errors` decorator that enables automatic reporting of failed assertions (supports pytest and unittest)

### Fixed

- Fixed issue with driver commands executed inside `WebDriverWait` loops being reported even when driver command reporting is disabled

## [0.63.14] - 2020-08-10

### Added

- Add a custom capability 'cloud:URL' usage documentation.

### Changed

- Ensure that only the `src` folder is included in a distribution.

### Fixed

- Fixed scenario when driver commands were not assigned to proper test.
- Fixed issue with test names being truncated at first space when running pytest parameterized tests.
- Fixed Safari driver initialization problem on macOS.

## [0.63.13] - 2020-07-15

### Added

- Added support for mobile (Android and iOS) automation.

### Changed

- Improved redaction of iOS and Android secure elements.

## [0.63.12] - 2020-07-10

### Changed

- Added _coming soon_ note to Appium references in README.

### Fixed

- Fixed extra test being added in report when manually reporting a test.
- Fixed test name being reported using class name instead of method name when using `unittest`.
- Fixed simple example presented in README file.

## [0.63.11] - 2020-07-08

First PyPI release.

### Fixed

- Fixed release version string

## [0.63.10]

Skipped.

## [0.63.9] - 2020-07-07

Initial release.