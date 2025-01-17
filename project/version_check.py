import pkg_resources

def check_versions(package_list):
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    for package in package_list:
        version = installed_packages.get(package.lower(), "Not installed")
        print(f"{package}: {version}")

# Replace these with the package names you want to check
selected_packages = ["zipfile", "shutil", "numpy", "pandas", "scikit-learn", "matplotlib", "sqlalchemy"]
check_versions(selected_packages)
