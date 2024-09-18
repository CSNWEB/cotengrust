# This file is automatically generated by pyo3_stub_gen
# ruff: noqa: E501, F401

import typing

def find_subgraphs(
    inputs: typing.Sequence[typing.Sequence[str]],
    output: typing.Sequence[str],
    size_dict: typing.Mapping[str, float],
) -> list[list[int]]:
    r"""
    Find all disconnected subgraphs of a specified contraction.
    """
    ...

def optimize_greedy(
    inputs: typing.Sequence[typing.Sequence[str]],
    output: typing.Sequence[str],
    size_dict: typing.Mapping[str, float],
    costmod: typing.Optional[float] = None,
    temperature: typing.Optional[float] = None,
    seed: typing.Optional[int] = None,
    simplify: typing.Optional[bool] = None,
    use_ssa: typing.Optional[bool] = None,
) -> list[list[int]]:
    r"""

    Find a contraction path using a (randomizable) greedy algorithm.

        Parameters
        ----------
        inputs : Sequence[Sequence[str]]
            The indices of each input tensor.
        output : Sequence[str]
            The indices of the output tensor.
        size_dict : dict[str, int]
            A dictionary mapping indices to their dimension.
        costmod : float, optional
            When assessing local greedy scores how much to weight the size of the
            tensors removed compared to the size of the tensor added::

                score = size_ab / costmod - (size_a + size_b) * costmod

            This can be a useful hyper-parameter to tune.
        temperature : float, optional
            When asessing local greedy scores, how much to randomly perturb the
            score. This is implemented as::

                score -> sign(score) * log(|score|) - temperature * gumbel()

            which implements boltzmann sampling.
        simplify : bool, optional
            Whether to perform simplifications before optimizing. These are:

                - ignore any indices that appear in all terms
                - combine any repeated indices within a single term
                - reduce any non-output indices that only appear on a single term
                - combine any scalar terms
                - combine any tensors with matching indices (hadamard products)

            Such simpifications may be required in the general case for the proper
            functioning of the core optimization, but may be skipped if the input
            indices are already in a simplified form.
        use_ssa : bool, optional
            Whether to return the contraction path in 'single static assignment'
            (SSA) format (i.e. as if each intermediate is appended to the list of
            inputs, without removals). This can be quicker and easier to work with
            than the 'linear recycled' format that `numpy` and `opt_einsum` use.

        Returns
        -------
        path : list[list[int]]
            The contraction path, given as a sequence of pairs of node indices. It
            may also have single term contractions if `simplify=True`.
    """
    ...

def optimize_optimal(
    inputs: typing.Sequence[typing.Sequence[str]],
    output: typing.Sequence[str],
    size_dict: typing.Mapping[str, float],
    minimize: typing.Optional[str] = None,
    cost_cap: typing.Optional[float] = None,
    search_outer: typing.Optional[bool] = None,
    simplify: typing.Optional[bool] = None,
    use_ssa: typing.Optional[bool] = None,
) -> list[list[int]]:
    r"""
    Find an optimal contraction ordering.

    Parameters
    ----------
    inputs : Sequence[Sequence[str]]
        The indices of each input tensor.
    output : Sequence[str]
        The indices of the output tensor.
    size_dict : dict[str, int]
        The size of each index.
    minimize : str, optional
        The cost function to minimize. The options are:

        - "flops": minimize with respect to total operation count only
          (also known as contraction cost)
        - "size": minimize with respect to maximum intermediate size only
          (also known as contraction width)
        - 'write' : minimize the sum of all tensor sizes, i.e. memory written
        - 'combo' or 'combo={factor}` : minimize the sum of
          FLOPS + factor * WRITE, with a default factor of 64.
        - 'limit' or 'limit={factor}` : minimize the sum of
          MAX(FLOPS, alpha * WRITE) for each individual contraction, with a
          default factor of 64.

        'combo' is generally a good default in term of practical hardware
        performance, where both memory bandwidth and compute are limited.
    cost_cap : float, optional
        The maximum cost of a contraction to initially consider. This acts like
        a sieve and is doubled at each iteration until the optimal path can
        be found, but supplying an accurate guess can speed up the algorithm.
    search_outer : bool, optional
        If True, consider outer product contractions. This is much slower but
        theoretically might be required to find the true optimal 'flops'
        ordering. In practical settings (i.e. with minimize='combo'), outer
        products should not be required.
    simplify : bool, optional
        Whether to perform simplifications before optimizing. These are:

            - ignore any indices that appear in all terms
            - combine any repeated indices within a single term
            - reduce any non-output indices that only appear on a single term
            - combine any scalar terms
            - combine any tensors with matching indices (hadamard products)

        Such simpifications may be required in the general case for the proper
        functioning of the core optimization, but may be skipped if the input
        indices are already in a simplified form.
    use_ssa : bool, optional
        Whether to return the contraction path in 'single static assignment'
        (SSA) format (i.e. as if each intermediate is appended to the list of
        inputs, without removals). This can be quicker and easier to work with
        than the 'linear recycled' format that `numpy` and `opt_einsum` use.

    Returns
    -------
    path : list[list[int]]
         The contraction path, given as a sequence of pairs of node indices. It
         may also have single term contractions if `simplify=True`.
    """
    ...

def optimize_random_greedy_track_flops(
    inputs: typing.Sequence[typing.Sequence[str]],
    output: typing.Sequence[str],
    size_dict: typing.Mapping[str, float],
    ntrials: int,
    costmod: typing.Optional[tuple[float, float]] = None,
    temperature: typing.Optional[tuple[float, float]] = None,
    seed: typing.Optional[int] = None,
    simplify: typing.Optional[bool] = None,
    use_ssa: typing.Optional[bool] = None,
) -> tuple[list[list[int]], float]:
    r"""
    Perform a batch of random greedy optimizations, simulteneously tracking
    the best contraction path in terms of flops, so as to avoid constructing a
    separate contraction tree.

    Parameters
    ----------
    inputs : tuple[tuple[str]]
        The indices of each input tensor.
    output : tuple[str]
        The indices of the output tensor.
    size_dict : dict[str, int]
        A dictionary mapping indices to their dimension.
    ntrials : int, optional
        The number of random greedy trials to perform. The default is 1.
    costmod : (float, float), optional
        When assessing local greedy scores how much to weight the size of the
        tensors removed compared to the size of the tensor added::

            score = size_ab / costmod - (size_a + size_b) * costmod

        It is sampled uniformly from the given range.
    temperature : (float, float), optional
        When asessing local greedy scores, how much to randomly perturb the
        score. This is implemented as::

            score -> sign(score) * log(|score|) - temperature * gumbel()

        which implements boltzmann sampling. It is sampled log-uniformly from
        the given range.
    seed : int, optional
        The seed for the random number generator.
    simplify : bool, optional
        Whether to perform simplifications before optimizing. These are:

            - ignore any indices that appear in all terms
            - combine any repeated indices within a single term
            - reduce any non-output indices that only appear on a single term
            - combine any scalar terms
            - combine any tensors with matching indices (hadamard products)

        Such simpifications may be required in the general case for the proper
        functioning of the core optimization, but may be skipped if the input
        indices are already in a simplified form.
    use_ssa : bool, optional
        Whether to return the contraction path in 'single static assignment'
        (SSA) format (i.e. as if each intermediate is appended to the list of
        inputs, without removals). This can be quicker and easier to work with
        than the 'linear recycled' format that `numpy` and `opt_einsum` use.

    Returns
    -------
    path : list[list[int]]
        The best contraction path, given as a sequence of pairs of node
        indices.
    flops : float
        The flops (/ contraction cost / number of multiplications), of the best
        contraction path, given log10.
    """
    ...

def optimize_simplify(
    inputs: typing.Sequence[typing.Sequence[str]],
    output: typing.Sequence[str],
    size_dict: typing.Mapping[str, float],
    use_ssa: typing.Optional[bool] = None,
) -> list[list[int]]:
    r"""

    Find the (partial) contracton path for simplifiactions only.

        Parameters
        ----------
        inputs : Sequence[Sequence[str]]
            The indices of each input tensor.
        output : Sequence[str]
            The indices of the output tensor.
        size_dict : dict[str, int]
            A dictionary mapping indices to their dimension.
        use_ssa : bool, optional
            Whether to return the contraction path in 'single static assignment'
            (SSA) format (i.e. as if each intermediate is appended to the list of
            inputs, without removals). This can be quicker and easier to work with
            than the 'linear recycled' format that `numpy` and `opt_einsum` use.

        Returns
        -------
        path : list[list[int]]
            The contraction path, given as a sequence of pairs of node indices. It
            may also have single term contractions.

    """
    ...

def ssa_to_linear(
    ssa_path: typing.Sequence[typing.Sequence[int]], n: typing.Optional[int] = None
) -> list[list[int]]:
    r"""
    Convert a SSA path to linear format.
    """
    ...
