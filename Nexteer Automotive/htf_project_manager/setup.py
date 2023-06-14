from setuptools import setup



setup(
    name="htfpm",
    packages=["htfpm"],
    include_package_data=True,
    version="0.0.0",
    license="proprietary",
    description="HilTestFramework",
    zip_safe=False,
    author="Nexteer/Poland/Tychy/EcuFunctionalVerificationTeam",
    python_requires='==3.8.*',
    options={"bdist_wheel": {"python_tag": "py38",
                             "plat_name": "win_amd64"}},
    install_requires=[
    ],
)
