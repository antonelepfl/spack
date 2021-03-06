# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FujitsuMpi(Package):
    """Fujitsu MPI implementation only for Fujitsu compiler."""

    homepage = "https://www.fujitsu.com/us/"

    conflicts('%arm')
    conflicts('%cce')
    conflicts('%clang')
    conflicts('%gcc')
    conflicts('%intel')
    conflicts('%nag')
    conflicts('%pgi')
    conflicts('%xl')
    conflicts('%xl_r')

    provides('mpi@3.1:')

    def install(self, spec, prefix):
        raise InstallError(
            'Fujitsu MPI is not installable; it is vendor supplied')

    def setup_dependent_package(self, module, dependent_spec):
        self.spec.mpicc = self.prefix.bin.mpifcc
        self.spec.mpicxx = self.prefix.bin.mpiFCC
        self.spec.mpif77 = self.prefix.bin.mpifrt
        self.spec.mpifc = self.prefix.bin.mpifrt

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('MPICC', self.prefix.bin.mpifcc)
        spack_env.set('MPICXX', self.prefix.bin.mpiFCC)
        spack_env.set('MPIF77', self.prefix.bin.mpifrt)
        spack_env.set('MPIF90', self.prefix.bin.mpifrt)
