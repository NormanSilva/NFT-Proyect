# Change Log
All notable changes to the "vscode-maven" extension will be documented in this file.

## 0.35.1

### Added
- Add shortcut for `test-compile` lifecycle. [#798](https://github.com/microsoft/vscode-maven/pull/798)
- Add tooltip showing path of POM file. [#799](https://github.com/microsoft/vscode-maven/pull/799)

### Fixed
- Fix completion of version. [#796](https://github.com/microsoft/vscode-maven/pull/796)

## 0.35.0

### Added
- Enable external call from other extensions to add dependencies. [#743](https://github.com/microsoft/vscode-maven/pull/743)
- Enable external call from other extensions to create Maven projects. [#775](https://github.com/microsoft/vscode-maven/pull/775)

### Fixed
- Custom options were not passed to the command line when creating new projects. [#771](https://github.com/microsoft/vscode-maven/issues/771)
- Failed to attach to remote debuggee VM when debugging a Maven goal. [#757](https://github.com/microsoft/vscode-maven/issues/757)
- Setting `maven.settingsFile` was not honored when executing Maven commands. [#776](https://github.com/microsoft/vscode-maven/pull/776)
- StackOverflowException when there exists circular dependencies in projects. [#763](https://github.com/microsoft/vscode-maven/issues/763)

## 0.34.2
### Fixed
- `Maven: Add a dependency` not working. [#766](https://github.com/microsoft/vscode-maven/issues/766)

## 0.34.1
### Fixed
- Update command for workspace trust management. [#749](https://github.com/microsoft/vscode-maven/pull/749)
- Update third party notices. [#751](https://github.com/microsoft/vscode-maven/pull/751)

## 0.34.0
### Added
- Add command to navigate between conflict dependencies. [#672](https://github.com/microsoft/vscode-maven/issues/672)
- New localization: Chinese (Traditional). [#727](https://github.com/microsoft/vscode-maven/pull/727)

### Changed
- Open POM file under local repository in readonly mode. [#718](https://github.com/microsoft/vscode-maven/issues/718)
- Improve performance on fetching plugin information. [#714](https://github.com/microsoft/vscode-maven/issues/714)

## 0.33.0
### Added
- New entry to `Run` lifecycle phases from context menu. [#700](https://github.com/microsoft/vscode-maven/issues/700)
- New setting `maven.projectOpenBehavior` specifying default way to open newly created project. [#662](https://github.com/microsoft/vscode-maven/issues/662)

### Fixed
- Bugs fixes and improvements related to dependency management.
  - Unified icons. [#707](https://github.com/microsoft/vscode-maven/issues/707)
  - New setting `maven.dependency.enableConflictDiagnostics` specifying whether to show diagnostics for dependency conflicts. [#677](https://github.com/microsoft/vscode-maven/issues/677)

## 0.32.2
### Fixed
- Failed to create project when an empty workspace is opened. [#689](https://github.com/microsoft/vscode-maven/issues/689)
- Malformed dependency node was inserted when pom.xml is dirty. [#690](https://github.com/microsoft/vscode-maven/pull/690) [#691](https://github.com/microsoft/vscode-maven/pull/691)

## 0.32.1
### Fixed
- A text file was wrongly created in workspace when calculating depenencies.

## 0.32.0
### Added
- [Preview] Improve dependency management experience. [#261](https://github.com/microsoft/vscode-maven/issues/261)
  - Visualize dependencies in Maven explorer.
  - Resolve dependency conflicts.

### Changed
- Present Effective POMs better with content provider API. [#680](https://github.com/microsoft/vscode-maven/pull/680)

### Fixed
- Environment varibles not loaded on calculating effective POM. [#637](https://github.com/microsoft/vscode-maven/issues/637)
- Effective POM was not update-to-date. [#681](https://github.com/microsoft/vscode-maven/pull/681)

## 0.31.0
### Added
- Add code action `add a dependency` when cursor is within `<dependencies>` node. [#634](https://github.com/microsoft/vscode-maven/pull/634)

### Fixed
- Fixed error when executing "Custom..." or "Favorites..." from command palette. [#628](https://github.com/microsoft/vscode-maven/pull/628)
- Fixed missing entries when resolving unknown types. [#638](https://github.com/microsoft/vscode-maven/pull/638)

## 0.30.1
### Fixed
- Fixed Maven project creation on Windows. [#623](https://github.com/microsoft/vscode-maven/issues/623)

## 0.30.0
### Changed
- Improved user experience for Maven project creation. [#604](https://github.com/microsoft/vscode-maven/issues/604)

### Fixed
- Archetype catalog could not be update. [#618](https://github.com/microsoft/vscode-maven/pull/618)

## 0.29.0
### Added
- Add shortcuts for common lifecycle phases into Maven explorer. [#601](https://github.com/microsoft/vscode-maven/pull/601)
- Add a new setting `maven.settingsFile` to specify location of settings.xml file. [#581](https://github.com/microsoft/vscode-maven/pull/581)

### Changed
- Only generate effective POMs on demand to improve overall performance. [#579](https://github.com/microsoft/vscode-maven/issues/579)
- Display project name, groupId, artifactId in Maven explorer. [#590](https://github.com/microsoft/vscode-maven/issues/590)

### Fixed
- Fix auto-completion for `version` section. [#594](https://github.com/microsoft/vscode-maven/issues/594)
- Fix auto-completion for `dependency` section when Java extension is working in lightweight mode. [#598](https://github.com/microsoft/vscode-maven/issues/598)
- Fix remote code execution vulnerability. [CVE-2021-28472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28472).

## 0.28.0
- Update extension icons. [#578](https://github.com/microsoft/vscode-maven/pull/578)
- Exclude POMs in `archetype-resources` folder by default. [#580](https://github.com/microsoft/vscode-maven/issues/580)
- Update setting `maven.terminal.customEnv` to only affect commands sent to terminal. [#584](https://github.com/microsoft/vscode-maven/pull/584) (Fix for [CVE-2021-27084](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-27084))

## 0.27.1
- Refine conceptual title of Maven explorer. [#567](https://github.com/microsoft/vscode-maven/pull/567)
- Improve UX of dependencies navigation. [#571](https://github.com/microsoft/vscode-maven/pull/571) [#572](https://github.com/microsoft/vscode-maven/pull/572) [#573](https://github.com/microsoft/vscode-maven/pull/573)

## 0.27.0
- Support to navigate to dependency POM file with `Ctrl/Cmd + Click`. [#562](https://github.com/microsoft/vscode-maven/pull/562)
- Use a unified command to create projects if Project Manager for Java is enabled. [#488](https://github.com/microsoft/vscode-maven/pull/488)
- Align with VS Code native UX. [#560](https://github.com/microsoft/vscode-maven/pull/560)

## 0.26.0
#### Changed
- Hide Maven Explorer for non-Maven workspaces. [#549](https://github.com/microsoft/vscode-maven/issues/549)
- No longer activate extension on opening xml files. [#555](https://github.com/microsoft/vscode-maven/pull/555)

#### Fixed
- Fix an error creating temporary directory for Remote-SSH scenario with multiple users. [#547](https://github.com/microsoft/vscode-maven/issues/547)
- Fix title of wizard for creating a project. [#551](https://github.com/microsoft/vscode-maven/issues/551)

## 0.25.0
#### Changed
- Allow users to hide the "Create Maven Project" entry in File Explorer. [#536](https://github.com/microsoft/vscode-maven/pull/536)
- Move "Open POM file" into context menu in Project Manager Explorer. [#541](https://github.com/microsoft/vscode-maven/pull/541)
#### Fixed
- Fix "Resolve unknown type" command when folder path contains whitespaces. [#535](https://github.com/microsoft/vscode-maven/pull/535)
- Fix path conversion when using WSL as default integrated terminal. [#542](https://github.com/microsoft/vscode-maven/pull/542)

## 0.24.2
#### Added
- Register entries for commands in Project Manager extension.
  - Add a dependency. [#529](https://github.com/microsoft/vscode-maven/pull/529)
  - Open POM file. [#530](https://github.com/microsoft/vscode-maven/pull/530)
  - Execute Maven Commands... [#531](https://github.com/microsoft/vscode-maven/pull/531)

## 0.24.1
#### Changed
- Change `maven.executable.options` to `machine-overridable` scope.
- Change `maven.executable.preferMavenWrapper` to `resource` scope.

## 0.24.0
#### Added
- Add back buttons to the project creation wizard. [#520](https://github.com/microsoft/vscode-maven/pull/520)

#### Fixed
- Settings `maven.executable.*` are now limited to machine scope. Fix for [CVE-2020-0604](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-0604).

## 0.23.0
#### Changed
- Rename project explorer. [#512](https://github.com/microsoft/vscode-maven/pull/512)
- Skip project selection when there is only one project. [#516](https://github.com/microsoft/vscode-maven/pull/516)

#### Fixed
- Fix: terminals were wrongly closed. [#513](https://github.com/microsoft/vscode-maven/pull/513)

## 0.22.0
#### Added
- Better support for PowerShell. [#494](https://github.com/microsoft/vscode-maven/pull/494)

#### Changed
- Keep the cache file of effective pom for diagnosis. [#319](https://github.com/microsoft/vscode-maven/issues/319#issuecomment-601494862)

#### Fixed
- Fix: mvnw was not identified if .mvn folder doesn't exist. [#504](https://github.com/microsoft/vscode-maven/issues/504)
- Fix: notification "Maven executable not found in PATH" pops up for multiple times. [#501](https://github.com/microsoft/vscode-maven/issues/501)
- Fix: tilde was not expanded as home directory in unix-like systems. [#507](https://github.com/microsoft/vscode-maven/pull/507)
- Fix: Maven output didn't write to the integrated terminal window. [#489](https://github.com/microsoft/vscode-maven/issues/489)

## 0.21.4
#### Fixed
- Set custom environment variables in folder level. [#487](https://github.com/microsoft/vscode-maven/issues/487)
- Better support for PowerShell Core. [#492](https://github.com/microsoft/vscode-maven/issues/492)

## 0.21.3
#### Fixed
- Update dependencies to fix vulnerability issues. [#481](https://github.com/microsoft/vscode-maven/pull/481) [#491](https://github.com/microsoft/vscode-maven/pull/491)

## 0.21.2
#### Fixed
- Destination folder was ingored when creating new project. [#478](https://github.com/microsoft/vscode-maven/issues/478)

## 0.21.1
#### Changed
- Reuse VS Code's icons. [#469](https://github.com/microsoft/vscode-maven/pull/469)

#### Fixed
- Terminals were opened in the wrong workspace root folder. [#467](https://github.com/microsoft/vscode-maven/issues/467)
- `NoClassDefFoundError` occurred when resolving unknown types. [#474](https://github.com/microsoft/vscode-maven/issues/474)

## 0.21.0
#### Added
- Support to debug favorite commands. [#444](https://github.com/microsoft/vscode-maven/issues/444)
- Add shortcut to view output when error occurs. [PR#458](https://github.com/microsoft/vscode-maven/pull/458)
- Support to browse to select local Maven executable if not found. [PR#457](https://github.com/microsoft/vscode-maven/pull/457)

#### Changed
- Remove unnecessary prefix `cmd /c` for powershell commands. [#452](https://github.com/microsoft/vscode-maven/issues/452)
- Walk up parent folders to find available Maven wrapper. [#PR460](https://github.com/microsoft/vscode-maven/pull/460)

#### Fixed
- Projects were not indexed when adding a folder to current workspace. [#453](https://github.com/microsoft/vscode-maven/issues/453)

## 0.20.2
#### Fixed
- Improve exposure of command "resolve unknown types". [PR#448](https://github.com/microsoft/vscode-maven/pull/448)

## 0.20.1
#### Fixed
- Insert the dependency into the wrong position when resolving unknown types. [#441](https://github.com/microsoft/vscode-maven/issues/441)

## 0.20.0
#### Added
- Support to "Collapse All" in Maven explorer. [PR#414](https://github.com/microsoft/vscode-maven/pull/414)
- Support to specify the project for command "Maven: Add a dependency". [PR418](https://github.com/microsoft/vscode-maven/pull/418)

#### Changed
- Update related icons in Maven explorer. [PR#425](https://github.com/microsoft/vscode-maven/pull/425)
- Upgrade embeded maven wrapper to 3.6.2. [PR#416](https://github.com/microsoft/vscode-maven/pull/416)

#### Fixed
- Java extension was unnecessarily activated. [#424](https://github.com/microsoft/vscode-maven/issues/424)
- Projects were not identified before expanding the Maven explorer. [#429](https://github.com/microsoft/vscode-maven/issues/429)

## 0.19.1
#### Added
- Provide more completion suggestions for groupId and artifactId on POM file authoring. [PR#404](https://github.com/microsoft/vscode-maven/pull/404)

#### Fixed
- No candidates when resolving unknown types. [PR#405](https://github.com/microsoft/vscode-maven/pull/405)

## 0.19.0
#### Added
- Add inline action buttons in Maven explorer.
- Add icons for Maven explorer items. [PR#397](https://github.com/microsoft/vscode-maven/pull/397)
- Can add dependencies when hovering on unresolved types. [PR#391](https://github.com/microsoft/vscode-maven/pull/391)

#### Fixed
- Cannot show dependencies.
- Expanded plugin nodes tend to collapse after loading. [#364](https://github.com/microsoft/vscode-maven/issues/364)

## 0.18.2
#### Fixed
- Typo in Hover information. [#368](https://github.com/microsoft/vscode-maven/issues/368)
- Unexpected error log on first use. [#358](https://github.com/microsoft/vscode-maven/issues/358)
- Switch to use new VS Code API (v1.37+) to get default shell. [#337](https://github.com/microsoft/vscode-maven/issues/337)

Thank [Christian Lutz @thccorni](https://github.com/thccorni) for contribution.

## 0.18.1
#### Fixed
- Cannot show plugin goals. [#340](https://github.com/microsoft/vscode-maven/issues/340)

## 0.18.0
#### Added
- For Maven project creation:
  - Fallback to use an embedded Maven wrapper if no availble Maven executable is found. [PR#344](https://github.com/microsoft/vscode-maven/pull/344)
  - Support to select archetype version. [#354](https://github.com/microsoft/vscode-maven/issues/354)
- Refresh explorer when config `maven.pomfile.globPattern` changes. [#334](https://github.com/microsoft/vscode-maven/issues/334)

#### Changed
- Change command name "Generate from Maven Archetype" to "Create Maven Project" for clarity. [#345](https://github.com/microsoft/vscode-maven/issues/345)

## 0.17.1
#### Fixed
- Provide a workaround for default shell detection. [#319](https://github.com/microsoft/vscode-maven/issues/319)

## 0.17.0
#### Added
- Add new config `maven.pomfile.globPattern`, which specifies how the extension searchs for POM files. [#316](https://github.com/microsoft/vscode-maven/issues/316)
- Add new config `maven.pomfile.autoUpdateEffectivePOM`, which specifies whether to update Effective-POM automatically. [#319](https://github.com/microsoft/vscode-maven/issues/319)

#### Fixed
- Unexpected insertion of code snippets. [#310](https://github.com/microsoft/vscode-maven/issues/310)
- A bug that Maven `localRepository` setting was not effective. [#322](https://github.com/microsoft/vscode-maven/issues/322)
- Cannot create Maven project when target directory has brackets and default shell is PowerShell. [#324](https://github.com/microsoft/vscode-maven/issues/324)

Thank [Justin Ridgewell (@jridgewell)](https://github.com/jridgewell) for the contributions to make the extension even better.

## 0.16.2
#### Fixed
- A regression issue which blocks auto-completion for pom files. [#311](https://github.com/Microsoft/vscode-maven/issues/311)

## 0.16.1
#### Fixed
- An error on calculating effective pom when there is whitespace in project path. [#304](https://github.com/Microsoft/vscode-maven/issues/304)
- A bug which causes to retry calculating effective pom all the time. [#296](https://github.com/Microsoft/vscode-maven/issues/296)

## 0.16.0
#### Added
- Support to debug a plugin goal.
  - The feature is designed for debugging code of the plugin goal itself. It can also debug Java classes loaded in the same JVM.
  - Debugging Java classes loaded by a forked process is not supported. E.g. when `devtools` is present, breakpoints in application code will not be hit when debugging `spring-boot:run` according to [its docs](https://docs.spring.io/spring-boot/docs/current/maven-plugin/run-mojo.html#fork).
- Add a shortcut to show dependency tree.

#### Fixed
- Fix miscellaneous minor issues by enabling TS strict null check.

## 0.15.2
#### Fixed
- A potential NPE when no f