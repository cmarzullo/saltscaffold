# saltscaffold

This python module creates a new directory structure for salt formulas with the following features:

* README.md with sample content
* state files that mimic the package / file / service pattern.
* .kitchen.yml with content to drive test-kitchen
* .kitchen-ci.yml with content to drive test-kitchen with alternate settings
* custom-pillar content to show pillar overrides
* defaults.yml content with default values
* map.jinja show how to have grains based overrides and merge defaults with custom pillars
* example of toggle feature
* The resulting formula will be testable with test-kitchen
* serverspec test to used with kitchen verify

## Folder and File Structure
Each salt formula that you scaffold will create the following folder structure:
```
[formula_name]/
[formula_name]/README.md
[formula_name]/pillar-custom.sls
[formula_name]/[formula_name]
[formula_name]/[formula_name]/defaults.yaml
[formula_name]/[formula_name]/map.jinja
[formula_name]/[formula_name]/init.sls
[formula_name]/[formula_name]/install.sls
[formula_name]/[formula_name]/config.sls
[formula_name]/[formula_name]/service.sls
[formula_name]/[formula_name]/files/
[formula_name]/[formula_name]/files/config.conf
[formula_name]/test/integration/default/serverspec/_spec.rb
```
It's expected you'll modify and rename these as you need.

## Installing saltscaffold

You can view the source code on the [Github Project Page](https://github.com/cmarzullo/saltsaffold)

### Install from source

  1. clone the repo `git clone https://github.com/cmarzullo/saltsaffold`
  2. make the packages `cd saltscaffold && python setup.py sdist`
  3. install the package `sudo pip install dist/Saltscaffold-<version>.tar.gz`

### Install from release

  1. Visit the [Bits Project Page](https://github.com/cmarzullo/saltsaffold)
  2. Click on Releases
  3. Download the latest release
  4. install the package `sudo pip install Saltscaffold-<version>.tar.gz`

## Running saltscaffold

The module gets installed as an executable python script. There aren't many options. You can only choose the name of the formula and an optional directory to create the formula in.

`saltscaffold -p myformula [-d {base directory} ]`

If you don't supply a base directory the formula will be created in your current directory.

## Contribution

Pull requests are welcome!

### Templating

It's kinda wierd to have to write jinja looking files with jinja. So I switched to the mako templating engine. 

### Running Tests

There are tests written. Make sure they pass. You can run tests using `nosetests -v`
There's no test for it, but make sure you can do a `kitchen verify`  with the output.
