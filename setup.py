from setuptools import find_packages, setup

package_name = 'learn_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tk',
    maintainer_email='tkmcbo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'gray_publisher = learn_pkg.gray_publisher:main',
            'image_publisher = learn_pkg.image_publisher:main',
            'edge_node = learn_pkg.edge_node:main',

        ],
    },
)
