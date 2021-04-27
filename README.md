# Pass-Clustering

Project template for clustering passes in football. Performs basic clustering (OPTICS algorithm) based on pass start+end location and angle; Presents results on the following visualization:
![plot](./result.png)

Repo doesn't contain any data parsing (or data) besides filtering progressive passes (a pass is progressive when it gets a team closer to the opposite goal by at least 25%). To run main.ipynb, you need to supply your own csv with passes (see _scripts/metadata.py for more info on the format) and field-plotting function (draw_field(matplotlib.axes.Axes ax) at _scripts/field.py).

What I would do with this project if I had time:
* **Automate viz generation** - Now it's mostly hardcoded which is fine since I used it once but would be nice if it supported more teams/other layouts and didn't require to change team names in hundred places.
* **Improve on clustering method** - I didn't really do much experimenting in this area, just used what worked for my combination project (https://wawrzynow.wordpress.com/2021/01/06/introducing-passing-combinations/) but there might be better algorithms/hyperparams/metrics to use here.
* **Engineer new features** - I thought of adding some more advanced features to the party (like e.g. whether a pass is made during a counter or a positional attack, maybe whether the ball is chipped etc). This could allow to capture even more context and produce even more insight but could harm explainability and possibly make the above vizualization useless.
* **Perform clustering on different types of passes** - basically do the thing from above but split passes before clustering (so cluster counter-attacking passes separately from the positional-attack ones etc). Would produce a great level of insight and a great visualization
