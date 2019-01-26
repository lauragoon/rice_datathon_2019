import animal_bite_parser
import emissions_parser
import matplotlib.pyplot as plt
import mplleaflet

animal_data = animal_bite_parser.use()
emissions_data = emissions_parser.use()

plt.hold(True)

plt.plot(animal_data[1], animal_data[0], "ro", markersize = "2")
plt.plot(emissions_data[1], emissions_data[0], "bo")

mplleaflet.show()

