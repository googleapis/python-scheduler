# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-scheduler/#history

## [2.2.0](https://www.github.com/googleapis/python-scheduler/compare/v2.1.1...v2.2.0) (2021-03-31)


### Features

* add `from_service_account_info` ([#67](https://www.github.com/googleapis/python-scheduler/issues/67)) ([bd21900](https://www.github.com/googleapis/python-scheduler/commit/bd2190046269eea1e08111b97f01e845f748b8e5))

### [2.1.1](https://www.github.com/googleapis/python-scheduler/compare/v2.1.0...v2.1.1) (2021-02-08)


### Bug Fixes

* remove client recv msg limit and add enums to `types/__init__.py` ([#46](https://www.github.com/googleapis/python-scheduler/issues/46)) ([b6a9feb](https://www.github.com/googleapis/python-scheduler/commit/b6a9feb31aec9ee1aa4eb46ccd44dcc8e6cc27a7))

## [2.1.0](https://www.github.com/googleapis/python-scheduler/compare/v2.0.0...v2.1.0) (2020-12-08)


### Features

* add common resource helpers; expose client transport ([#41](https://www.github.com/googleapis/python-scheduler/issues/41)) ([f9fc0f9](https://www.github.com/googleapis/python-scheduler/commit/f9fc0f9613302de642680c87286de0a02f09d086))

## [2.0.0](https://www.github.com/googleapis/python-scheduler/compare/v1.3.0...v2.0.0) (2020-08-27)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#29)

### Features

* migrate to microgenerator ([#29](https://www.github.com/googleapis/python-scheduler/issues/29)) ([82f66ed](https://www.github.com/googleapis/python-scheduler/commit/82f66ed9c163b2f6597bf5661469ca9ca1bef741))


### Bug Fixes

* update retry configs ([#20](https://www.github.com/googleapis/python-scheduler/issues/20)) ([7f82c9f](https://www.github.com/googleapis/python-scheduler/commit/7f82c9ffc292d72907de66bf6d5fa39e38d26085))

## [1.3.0](https://www.github.com/googleapis/python-scheduler/compare/v1.2.1...v1.3.0) (2020-04-21)


### ⚠ BREAKING CHANGES

* **scheduler:** remove `project_path` method, update docstrings (via synth) (#9522)

### Bug Fixes

* **scheduler:** remove `project_path` method, update docstrings (via synth) ([#9522](https://www.github.com/googleapis/python-scheduler/issues/9522)) ([36c611b](https://www.github.com/googleapis/python-scheduler/commit/36c611bdd1504918ecec39f7846c533b1e7b181c))
* add python 2.7 deprecation warning (via synth) ([#9](https://www.github.com/googleapis/python-scheduler/issues/9)) ([d17f5ff](https://www.github.com/googleapis/python-scheduler/commit/d17f5ffd8d6030190e3529d6eed5c9899145dd96))

## 1.2.1

08-12-2019 13:53 PDT

### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8966](https://github.com/googleapis/google-cloud-python/pull/8966))

### Documentation
- Fix links to googleapis.dev ([#8998](https://github.com/googleapis/google-cloud-python/pull/8998))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 1.2.0

07-24-2019 17:27 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth).  ([#8401](https://github.com/googleapis/google-cloud-python/pull/8401))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8520](https://github.com/googleapis/google-cloud-python/pull/8520))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Pin black version (via synth). ([#8593](https://github.com/googleapis/google-cloud-python/pull/8593))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

### Internal / Testing Changes
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8361](https://github.com/googleapis/google-cloud-python/pull/8361))
- Add disclaimer to auto-generated template (via synth). ([#8325](https://github.com/googleapis/google-cloud-python/pull/8325))
- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8250](https://github.com/googleapis/google-cloud-python/pull/8250))
- Fix coverage in 'types.py' (via synth). ([#8162](https://github.com/googleapis/google-cloud-python/pull/8162))
- Blacken noxfile.py, setup.py (via synth). ([#8130](https://github.com/googleapis/google-cloud-python/pull/8130))
- Add empty lines (via synth). ([#8069](https://github.com/googleapis/google-cloud-python/pull/8069))

## 1.1.0

05-13-2019 13:15 PDT

### New Features
- Add authorization headers and deadline for job attempts (via synth). ([#7938](https://github.com/googleapis/google-cloud-python/pull/7938))

### Internal / Testing Changes
- Add nox session `docs`, reorder methods (via synth). ([#7779](https://github.com/googleapis/google-cloud-python/pull/7779))

## 1.0.0

05-03-2019 10:04 PDT

### Internal / Testing Changes
- Add smoke test for scheduler. ([#7854](https://github.com/googleapis/google-cloud-python/pull/7854))

## 0.3.0

04-15-2019 10:32 PDT


### New Features
- add auth and configurable timeouts to v1beta1 (via synth). ([#7665](https://github.com/googleapis/google-cloud-python/pull/7665))

## 0.2.0

04-01-2019 15:39 PDT


### Implementation Changes
- Add routing header to method metadata (via synth). ([#7599](https://github.com/googleapis/google-cloud-python/pull/7599))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Remove unused message exports. ([#7273](https://github.com/googleapis/google-cloud-python/pull/7273))
- Protoc-generated serialization update. ([#7093](https://github.com/googleapis/google-cloud-python/pull/7093))
- Protoc-generated serialization update. ([#7055](https://github.com/googleapis/google-cloud-python/pull/7055))
- Use moved iam.policy now at google.api_core.iam.policy. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))

### New Features
- Add v1. ([#7608](https://github.com/googleapis/google-cloud-python/pull/7608))
- Pick up fixes to GAPIC generator. ([#6505](https://github.com/googleapis/google-cloud-python/pull/6505))

### Documentation
- googlecloudplatform --> googleapis in READMEs. ([#7411](https://github.com/googleapis/google-cloud-python/pull/7411))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Update copyright year. ([#7155](https://github.com/googleapis/google-cloud-python/pull/7155))
- Correct a link in a documentation string. ([#7119](https://github.com/googleapis/google-cloud-python/pull/7119))
- Pick up stub docstring fix in GAPIC generator. ([#6980](https://github.com/googleapis/google-cloud-python/pull/6980))
- Document Python 2 deprecation. ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Update link for Scheduler Docs. ([#6925](https://github.com/googleapis/google-cloud-python/pull/6925))

### Internal / Testing Changes
- Copy lintified proto files (via synth). ([#7469](https://github.com/googleapis/google-cloud-python/pull/7469))
- Add clarifying comment to blacken nox target. ([#7401](https://github.com/googleapis/google-cloud-python/pull/7401))
- Add protos as an artifact to library. ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Add baseline for synth.metadata. ([#6792](https://github.com/googleapis/google-cloud-python/pull/6865))
- Update noxfile. ([#6814](https://github.com/googleapis/google-cloud-python/pull/6814))
- Blacken all gen'd libs. ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps. ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py. ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries. ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))

## 0.1.0

11-13-2018 11:03 PST


### New Features
- Initial release of Cloud Scheduler library. ([#6482](https://github.com/googleapis/google-cloud-python/pull/6482))
