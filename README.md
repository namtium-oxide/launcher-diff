# launcher-diff

Find changes in official Minecraft version manifests.

## Result

Last updated: July 13, 2021

```
launcher version: 4
+ /assetIndex/id(str)
+ /assetIndex/sha1(str)
+ /assetIndex/size(int)
+ /assetIndex/totalSize(int)
+ /assetIndex/url(str)
+ /assets(str)
+ /downloads/client/sha1(str)
+ /downloads/client/size(int)
+ /downloads/client/url(str)
+ /downloads/server/sha1(str)
+ /downloads/server/size(int)
+ /downloads/server/url(str)
+ /downloads/windows_server/sha1(str)
+ /downloads/windows_server/size(int)
+ /downloads/windows_server/url(str)
+ /id(str)
+ /libraries/*/downloads/artifact/path(str)
+ /libraries/*/downloads/artifact/sha1(str)
+ /libraries/*/downloads/artifact/size(int)
+ /libraries/*/downloads/artifact/url(str)
+ /libraries/*/downloads/classifiers/natives-linux/path(str)
+ /libraries/*/downloads/classifiers/natives-linux/sha1(str)
+ /libraries/*/downloads/classifiers/natives-linux/size(int)
+ /libraries/*/downloads/classifiers/natives-linux/url(str)
+ /libraries/*/downloads/classifiers/natives-osx/path(str)
+ /libraries/*/downloads/classifiers/natives-osx/sha1(str)
+ /libraries/*/downloads/classifiers/natives-osx/size(int)
+ /libraries/*/downloads/classifiers/natives-osx/url(str)
+ /libraries/*/downloads/classifiers/natives-windows/path(str)
+ /libraries/*/downloads/classifiers/natives-windows/sha1(str)
+ /libraries/*/downloads/classifiers/natives-windows/size(int)
+ /libraries/*/downloads/classifiers/natives-windows/url(str)
+ /libraries/*/extract/exclude/*(str)
+ /libraries/*/name(str)
+ /libraries/*/natives/linux(str)
+ /libraries/*/natives/osx(str)
+ /libraries/*/natives/windows(str)
+ /libraries/*/rules/*/action(str)
+ /libraries/*/rules/*/os/name(str)
+ /libraries/*/rules/*/os/version(str)
+ /mainClass(str)
+ /minecraftArguments(str)
+ /minimumLauncherVersion(int)
+ /releaseTime(str)
+ /time(str)
+ /type(str)

launcher version: 7
+ /complianceLevel(int)
+ /javaVersion/component(str)
+ /javaVersion/majorVersion(int)
+ /logging/client/argument(str)
+ /logging/client/file/id(str)
+ /logging/client/file/sha1(str)
+ /logging/client/file/size(int)
+ /logging/client/file/url(str)
+ /logging/client/type(str)

launcher version: 9
- /libraries/*/rules/*/os/version(str)

launcher version: 10
+ /libraries/*/downloads/classifiers/natives-windows-32/path(str)
+ /libraries/*/downloads/classifiers/natives-windows-32/sha1(str)
+ /libraries/*/downloads/classifiers/natives-windows-32/size(int)
+ /libraries/*/downloads/classifiers/natives-windows-32/url(str)
+ /libraries/*/downloads/classifiers/natives-windows-64/path(str)
+ /libraries/*/downloads/classifiers/natives-windows-64/sha1(str)
+ /libraries/*/downloads/classifiers/natives-windows-64/size(int)
+ /libraries/*/downloads/classifiers/natives-windows-64/url(str)

launcher version: 11

launcher version: 12

launcher version: 13

launcher version: 14

launcher version: 18
+ /arguments/game/*(str)
+ /arguments/game/*/rules/*/action(str)
+ /arguments/game/*/rules/*/features/has_custom_resolution(bool)
+ /arguments/game/*/rules/*/features/is_demo_user(bool)
+ /arguments/game/*/value(str)
+ /arguments/game/*/value/*(str)
+ /arguments/jvm/*(str)
+ /arguments/jvm/*/rules/*/action(str)
+ /arguments/jvm/*/rules/*/os/name(str)
+ /arguments/jvm/*/rules/*/os/version(str)
+ /arguments/jvm/*/value(str)
+ /arguments/jvm/*/value/*(str)
+ /libraries/*/downloads/classifiers/javadoc/path(str)
+ /libraries/*/downloads/classifiers/javadoc/sha1(str)
+ /libraries/*/downloads/classifiers/javadoc/size(int)
+ /libraries/*/downloads/classifiers/javadoc/url(str)
+ /libraries/*/downloads/classifiers/natives-macos/path(str)
+ /libraries/*/downloads/classifiers/natives-macos/sha1(str)
+ /libraries/*/downloads/classifiers/natives-macos/size(int)
+ /libraries/*/downloads/classifiers/natives-macos/url(str)
+ /libraries/*/downloads/classifiers/sources/path(str)
+ /libraries/*/downloads/classifiers/sources/sha1(str)
+ /libraries/*/downloads/classifiers/sources/size(int)
+ /libraries/*/downloads/classifiers/sources/url(str)
- /downloads/windows_server/sha1(str)
- /downloads/windows_server/size(int)
- /downloads/windows_server/url(str)
- /libraries/*/downloads/classifiers/natives-windows-32/path(str)
- /libraries/*/downloads/classifiers/natives-windows-32/sha1(str)
- /libraries/*/downloads/classifiers/natives-windows-32/size(int)
- /libraries/*/downloads/classifiers/natives-windows-32/url(str)
- /libraries/*/downloads/classifiers/natives-windows-64/path(str)
- /libraries/*/downloads/classifiers/natives-windows-64/sha1(str)
- /libraries/*/downloads/classifiers/natives-windows-64/size(int)
- /libraries/*/downloads/classifiers/natives-windows-64/url(str)

launcher version: 21
+ /arguments/jvm/*/rules/*/os/arch(str)
+ /downloads/client_mappings/sha1(str)
+ /downloads/client_mappings/size(int)
+ /downloads/client_mappings/url(str)
+ /downloads/server_mappings/sha1(str)
+ /downloads/server_mappings/size(int)
+ /downloads/server_mappings/url(str)
- /minecraftArguments(str)

```