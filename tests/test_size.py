import pytest

params = []

params.append(pytest.param(4, 4, marks=[pytest.mark.mpi(min_size=4)]))
params.append(pytest.param(6, 6, marks=[pytest.mark.mpi(min_size=6)]))
params.append(pytest.param(16, 16, marks=[pytest.mark.mpi(min_size=16)]))
params.append(pytest.param(20, 20, marks=[pytest.mark.mpi(min_size=20)]))


@pytest.mark.parametrize("sz,comm_split_fixture", params, indirect=["comm_split_fixture"])
def test_get_size(barrier_fence_fixture, sz, comm_split_fixture):

    import test_mpi_pkg

    # Isolate the minimum needed ranks
    base_comm, active = comm_split_fixture
    if not active:
        return

    rsz = test_mpi_pkg.get_size(base_comm)

    assert(sz == rsz)
