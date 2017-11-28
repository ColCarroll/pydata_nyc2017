import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline


def gen_polynomial(x_original, degree=4):
    """Takes a vector and generates polynomial features for it."""
    pipe = make_pipeline(PolynomialFeatures(degree=degree),
                         StandardScaler(with_mean=False))
    pipe.fit(x_original)

    return pipe.transform, pipe.named_steps['standardscaler'].scale_


def plotter(x, y, fit_fn=None, transform=None, noise=None):
    line_kwargs = {'color': 'blue'}
    dot_kwargs = {'alpha': 0.5}
    if fit_fn:
        if transform is None:
            transform = lambda j: j
        x_data = np.atleast_2d(np.linspace(x.min(), x.max(), num=500)).T
        y_fit = fit_fn(transform(x_data))
        if y_fit.ndim == 2 and y_fit.shape[1] > 1:
            n_lines = y_fit.shape[1]
            if n_lines > 100:
                indices = np.linspace(0, n_lines - 1, num=100, dtype=int)
                y_fit = y_fit[:, indices]
                n_lines = len(indices)
            line_kwargs['alpha'] = 0.3
            line_kwargs['linewidth'] = 2
            x_data = np.repeat(np.atleast_2d(x_data), n_lines, axis=1)
        plt.plot(x_data, y_fit, '-', **line_kwargs)
        if noise is not None:
            noise = noise[indices]
            noise_kwargs = line_kwargs.copy()
            noise_kwargs['color'] = 'steelblue'
            noise_kwargs['linewidth'] = line_kwargs['linewidth'] * 0.5
            for const in (-2, -1, 1, 2):
                noise_kwargs['alpha'] = 0.5 * line_kwargs['alpha'] / abs(const)
                plt.plot(x_data, y_fit + const * noise, '-', **noise_kwargs)
    plt.plot(x, y, 'ro', **dot_kwargs)


def get_overfitting_data():
    x, y, _, _, _ = get_base_data()
    noise = get_noise()
    np.random.seed(58)
    x_train, x_test, y_train, y_test = train_test_split(x, y + noise, test_size=80)
    transform, scale = gen_polynomial(x_train, 14)
    X_train = transform(x_train)
    X_test = transform(x_test)
    return x_train, x_test, y_train, y_test, X_train, X_test, transform, scale


def get_base_data():
    np.random.seed(58)

    x = np.atleast_2d(np.sort(6 * np.random.rand(100) - 3)).T
    y = x**3 + x**2 - 4 * x
    transform, scale = gen_polynomial(x, degree=3)
    X = transform(x)

    return x, y, X, transform, scale


def get_noise():
    np.random.seed(58)
    _, y, _, _, _ = get_base_data()
    return np.random.randn(*y.shape)
