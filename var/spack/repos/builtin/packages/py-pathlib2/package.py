# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPathlib2(PythonPackage):
    """Backport of pathlib from python 3.4"""

    homepage = "https://pypi.python.org/pypi/pathlib2"
    url      = "https://pypi.io/packages/source/p/pathlib2/pathlib2-2.3.5.tar.gz"

    import_modules = ['pathlib2']

    version('2.3.5', sha256='6cd9a47b597b37cc57de1c05e56fb1a1c9cc9fab04fe78c29acd090418529868')
    version('2.3.2', sha256='8eb170f8d0d61825e09a95b38be068299ddeda82f35e96c3301a8a5e7604cb83')
    version('2.1.0', sha256='deb3a960c1d55868dfbcac98432358b92ba89d95029cddd4040db1f27405055c')

    depends_on('py-setuptools', type='build')
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-scandir', when='^python@:3.4', type=('build', 'run'))
