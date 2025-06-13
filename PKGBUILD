# Maintainer: minhmc2007 <quangminh21072010@gmail.com>
# Contributor: Erik Dubois & Brad Heffernan (ArcoLinux Team)

pkgname=blue-archive-welcome-app
_pkgname=blue-archive-linux-welcome-app
pkgver=1.0.0
pkgrel=1
pkgdesc="Welcome application for Blue Archive Linux"
arch=('any')
url="https://github.com/minhmc2007/Blue-Archive-Linux"
license=('GPL3')
depends=('python-gobject' 'gtk3' 'python-psutil' 'rate-mirrors' 'alacritty')
makedepends=('git')
source=("${_pkgname}::git+https://github.com/minhmc2007/${_pkgname}.git")
sha256sums=('SKIP')

package() {
  cd "$_pkgname"

  # The Executable
  install -Dm755 "usr/local/bin/blue-archive-welcome-app" "$pkgdir/usr/local/bin/blue-archive-welcome-app"

  # The Python App & Image Files
  install -d "$pkgdir/usr/share/blue-archive-welcome-app"
  cp -r usr/share/blue-archive-welcome-app/* "$pkgdir/usr/share/blue-archive-welcome-app/"

  # The .desktop file for your application menu
  install -Dm644 "usr/share/applications/blue-archive-welcome-app.desktop" "$pkgdir/usr/share/applications/blue-archive-welcome-app.desktop"
  
  # The icon for the application menu
  install -Dm644 "usr/share/blue-archive-welcome-app/images/bal-icon.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/blue-archive-welcome-icon.png"

  # The license file
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
