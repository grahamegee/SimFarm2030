from core.model_daily_3d import cultivarModel
import numpy as np


def mock_seed_generator(a, b, c):
    return np.array([
        [1.19999942e+03, 9.99989596e+01, 7.00000406e+02, 1.49999807e+02,
         1.49999955e+03, 1.50001092e+02, -9.97483854e-02, 1.00553647e-01,
         -9.98953000e-02],
        [1.19999994e+03, 1.00001472e+02, 7.00000148e+02, 1.50000241e+02,
         1.50000178e+03, 1.50000746e+02, -1.03385249e-01, 1.00586755e-01,
         -9.93669151e-02],
        [1.20000026e+03, 1.00000097e+02, 6.99999791e+02, 1.49998613e+02,
         1.50000003e+03, 1.50000517e+02, -1.00289830e-01, 9.95485757e-02,
         -9.99780275e-02],
        [1.19999885e+03, 1.00001156e+02, 6.99999317e+02, 1.49999221e+02,
         1.50000050e+03, 1.49999512e+02, -9.87272941e-02, 1.00486185e-01,
         -1.01035595e-01],
        [ 1.19999866e+03, 1.00000193e+02, 7.00000362e+02, 1.49999462e+02,
         1.49999856e+03, 1.49998902e+02, -9.90940997e-02, 1.00492591e-01,
         -1.00440389e-01],
        [1.19999899e+03, 9.99996948e+01, 7.00001602e+02, 1.50000818e+02,
         1.50000053e+03, 1.50000652e+02, -9.97447458e-02, 1.00461503e-01,
         -1.01636842e-01],
        [1.19999994e+03, 1.00000549e+02, 6.99998686e+02, 1.50000570e+02,
         1.50000137e+03, 1.49998388e+02, -9.90384071e-02, 9.97407405e-02,
         -1.02177002e-01],
        [1.20000064e+03, 9.99982857e+01, 7.00000619e+02, 1.50000510e+02,
         1.50000134e+03, 1.50001506e+02, -1.00607706e-01, 9.95738841e-02,
         -9.78244537e-02],
        [ 1.19999868e+03, 1.00000161e+02, 7.00001615e+02, 1.50000247e+02,
         1.50000141e+03, 1.50001273e+02, -9.91108349e-02, 9.97173872e-02,
         -9.98472711e-02],
        [1.19999954e+03, 1.00000158e+02, 6.99999080e+02, 1.50000570e+02,
         1.49999956e+03, 1.49998218e+02, -1.00530397e-01, 1.01886254e-01,
         -1.00846299e-01],
        [1.20000075e+03, 9.99995520e+01, 7.00000305e+02, 1.49998956e+02,
         1.49999841e+03, 1.49999637e+02, -9.90344228e-02, 1.00840729e-01,
         -9.91352496e-02],
        [1.20000063e+03, 1.00000588e+02, 7.00001328e+02, 1.49999834e+02,
         1.50000231e+03, 1.49999932e+02, -9.85686235e-02, 1.00758141e-01,
         -9.87114193e-02],
        [1.19999882e+03, 1.00001196e+02, 6.99998988e+02, 1.49998803e+02,
         1.50000126e+03, 1.49999608e+02, -9.97553223e-02, 1.01152301e-01,
         -9.95391432e-02],
        [1.20000004e+03, 9.99994445e+01, 6.99999051e+02, 1.49999624e+02,
         1.49999856e+03, 1.49999155e+02, -1.00409122e-01, 1.00669367e-01,
         -1.00359962e-01],
        [1.20000031e+03, 9.99976547e+01, 6.99999755e+02, 1.49999809e+02,
         1.49999965e+03, 1.50000038e+02, -1.00540784e-01, 1.01005872e-01,
         -9.98984651e-02],
        [1.20000028e+03, 9.99992184e+01, 7.00000431e+02, 1.49998842e+02,
         1.50000013e+03, 1.49999222e+02, -1.00300363e-01, 1.00400500e-01,
         -1.00192447e-01],
        [1.20000050e+03, 1.00001498e+02, 7.00000669e+02, 1.50000102e+02,
         1.50000196e+03, 1.50002106e+02, -1.00784616e-01, 9.95052202e-02,
         -1.02061931e-01],
        [1.20000008e+03, 1.00001996e+02, 6.99998178e+02, 1.50001021e+02,
         1.50000063e+03, 1.50000464e+02, -1.00628242e-01, 1.01640565e-01,
         -9.84238101e-02],
        [1.20000063e+03, 9.99993080e+01, 7.00002029e+02, 1.50000043e+02,
         1.50000037e+03, 1.49998226e+02, -9.89521155e-02, 1.00238013e-01,
         -1.01675730e-01],
        [1.20000026e+03, 9.99984005e+01, 6.99999272e+02, 1.49998755e+02,
         1.50000028e+03, 1.50001188e+02, -9.80437237e-02, 9.91752224e-02,
         -9.83452450e-02],
        [1.20000238e+03, 9.99991596e+01, 7.00001695e+02, 1.50000332e+02,
         1.50000023e+03, 1.50000230e+02, -1.00187396e-01, 1.02216794e-01,
         -9.91931035e-02],
        [1.19999921e+03, 1.00000239e+02, 6.99999243e+02, 1.49999338e+02,
         1.50000092e+03, 1.49999388e+02, -1.00981203e-01, 9.91625809e-02,
         -9.82417043e-02],
        [1.20000148e+03, 1.00001504e+02, 7.00000950e+02, 1.50001032e+02,
         1.50000039e+03, 1.49999842e+02, -1.00252861e-01, 9.87003344e-02,
         -9.99628267e-02],
        [1.20000025e+03, 9.99992986e+01, 7.00000607e+02, 1.49999416e+02,
         1.49999976e+03, 1.50000564e+02, -1.00267221e-01, 1.01380211e-01,
         -1.00690097e-01],
        [1.20000050e+03, 9.99994066e+01, 6.99999252e+02, 1.49999205e+02,
         1.49999977e+03, 1.50000112e+02, -1.00100551e-01, 1.00144257e-01,
         -9.99394848e-02]
    ])


def test_training():
    cult = 'Test'
    simfarm = cultivarModel(
        cult, region_tol=0.25, metric='Yield',
        metric_units='t Ha$^{-1}$', seed_generator=mock_seed_generator)
    simfarm.train_and_validate_model(nsample=1100, nwalkers=25)
    assert np.mean(simfarm.resi) != np.nan
    assert np.median(simfarm.resi) != np.nan
    assert 0.2 <= simfarm.af <= 0.5
    assert all(v != np.nan for v in simfarm.mean_params.values())
    # assert simfarm.resi == [12.1234, 23.434, 56.3343]
