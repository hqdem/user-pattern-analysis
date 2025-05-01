from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r", encoding="utf-8-sig") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="chatcluster",
    version="0.1.0",
    description="Классификация и кластеризация паттернов общения",
    author="Твоё Имя",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    python_requires=">=3.8",
)
