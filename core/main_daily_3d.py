from model_daily_3d import cultivarModel
import utilities
import time
import pickle
import sys
import os


def get_non_hidden_filepaths():
    return [
        f for f in os.listdir('../example_data')
        if not f.startswith('.')
    ]


# Extract cultivar from command line input
cult = sys.argv[1]

if cult == "All":
    files = get_non_hidden_filepaths()
else:
    files = [cult + "_Data.csv", ]

for f in files:

    cult = f.split("_")[0]
    print(cult)

    tstart = time.time()
    simfarm = cultivarModel(cult, region_tol=0.25, metric='Yield',
                            metric_units='t Ha$^{-1}$')
    simfarm.train_and_validate_model(nsample=75000, nwalkers=250)
    print('Train', time.time() - tstart)

    simfarm.plot_walkers()
    simfarm.plot_response()
    simfarm.true_pred_comp()
    simfarm.climate_dependence()

    # Write out object as pickle
    with open('../cultivar_models/' + simfarm.cult + '_' + simfarm.metric
              + '_model_daily_3d.pck', 'wb') as pfile1:
        pickle.dump(simfarm, pfile1)

    simfarm.post_prior_comp()

    tau = simfarm.model.get_autocorr_time()
    print("Steps until initial start 'forgotten'", tau)
