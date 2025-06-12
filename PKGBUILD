# Maintainer: minhmc2007 <quangminh21072010@gmail.com>
# Contributor: Erik Dubois <erik.dubois@arcolinux.info>

# OLD
# pkgname=arcolinux-welcome-app
# NEW
pkgname=blue-archive-welcome-app

pkgver=24.05.01
pkgrel=1

# OLD
# pkgdesc="Welcome application for ArcoLinux"
# NEW
pkgdesc="Welcome application for Blue Archive Linux"

arch=('any')
# OLD
# url="https://github.com/arcolinux/arcolinux-welcome-app"
# NEW - Put your fork's URL here
url="https://github.com/minhmc2007/blue-archive-linux-welcome-app"

license=('GPL3')
depends=('python-gobject' 'gtk3' 'python-psutil')
makedepends=('git')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
  cd "$srcdir/$pkgname-$pkgver"

  # The 'install' command creates directories and copies files with the right permissions.
  # Notice how we use the NEW names here.

  # The Executable
  install -Dm755 "usr/local/bin/blue-archive-welcome-app" "$pkgdir/usr/local/bin/blue-archive-welcome-app"

  # The Python App & Image Files
  install -d "$pkgdir/usr/share/blue-archive-welcome-app"
  cp -r usr/share/blue-archive-welcome-app/* "$pkgdir/usr/share/blue-archive-welcome-app/"

  # The .desktop file for your application menu
  install -Dm644 "usr/share/applications/blue-archive-welcome-app.desktop" "$pkgdir/usr/share/applications/blue-archive-welcome-app.desktop"

  # The license file
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
