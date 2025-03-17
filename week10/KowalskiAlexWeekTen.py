# In billions of people
DEFAULT_COLINIZATION_POTENTIAL = 6

class SolarObject:
    # AU (Austronomical Units)
    farthest_distance: float;

    name: str;

    average_orbit_period: float;
    orbit_period_units: str;

    def __init__(self,
        name: str,
        farthest_distance: float,
        average_orbit_period: float
    ) -> None:
        self.name = name;
        self.farthest_distance = farthest_distance;
        self.average_orbit_period = average_orbit_period;

    def colonization(self) -> float:
        return DEFAULT_COLINIZATION_POTENTIAL/self.farthest_distance;

    # TLDR: used `return "circular";` instead of `pass;` for ergonomic reasons.
    #
    # So I'm having a bit of trouble with the directions given to us for
    # this assignment.
    #
    # The directions state that we must use the `pass` keyword in the
    # parent's `spin` method. However, this severly limits the usability
    # of overrides in child classes. This is because the `pass`
    # keyword implicitly returns `None` (when used in a function or method),
    # which thus restricts the return type for overrides to `None`.
    # So then, the only way of actually using the `pass` keyword in the
    # parent's method, is by forcing override methods in child classes to
    # print the orbit pattern, instead of just returning it. This severly
    # undermines the ergonmics and usability of this method.
    #
    # For example, I may want to store the orbit pattern of different
    # `SolarObject`'s in a list or even just write them to a file:
    # ```
    #    file.write(mars.spin());
    # ```
    # thus explaining how such a method would be limited in its uses.
    #
    # However it can be argued that since we're just gonna be printing
    # the orbit patterns either way and nothing more, it should be fine
    # to just print it in their respective overrides. Except, this
    # results in having to rely on how each override prints the value, leading
    # to code that may look like this:
    # ```
    #   spin(self):
    #       print("like crazy");
    #
    #   ...
    #
    #   print("Orbit Pattern: ");
    #   mars.spin();
    #   [other properties...]
    # ```
    # thus explaining how such a method would not be ergonmic as well.
    #
    # Although the solution I landed on is still somewhat suboptimal (it's
    # probably better to just have `spin` be a regular attribute like `name`
    # or `farthest_distance`), it at least holds some integrity
    # to the original intent of the directions, since I'm still defining a
    # `spin` method to be overridden in child classes, following
    # polymorphism principles.
    # So in order for our overrides to return stuff, we have to define a
    # `str` return type, as well as return something of said type in the parent's
    # method (which in this case I'll just return "circular"). Trying to
    # get around either of these requirements to attempt to use `pass` in the
    # parent method results in two possible errors:
    # 1. "Method `spin` overrides class `SolarObject` in an incompatible
    # manner: Return type mismatch"
    # or
    # 2. "Function with declared return type `str` must return a value on
    # all code paths: `None` is not assignable to `str`"
    #
    # The first happens because using `pass` without an explicit return types
    # implicitly limits the parent function, and by extension overrides, to
    # return `None`. The second error happens when trying to give the parent
    # function an explicit return type of `str`, but as stated before, using
    # `pass` in a function implicitly returns `None` which can't be a string.
    # So then I've opted to just return "circular" in the parent method,
    # as well as giving it an explicit return type of `str`.
    #
    # None of this probably matters, I just wanted to make my intentions clear
    # by deciding to not use `pass` in my parent method, ignoring given
    # instructions.
    def spin(self) -> str:
        return "circular";

    # Helper function for final presentation
    def display_solar_object(self):
        print(f"Object: {self.name}");
        print(f"Distance from Sun: {self.farthest_distance} AU");
        print(f"Orbit Pattern: {self.spin()}");
        print(f"Average Orbital Period: {self.average_orbit_period} {self.orbit_period_units}");
        formatted_num = "{:.3}".format(self.colonization());
        print(f"Colinization Potential: {formatted_num} billion people\n");

class Planet(SolarObject):
    orbit_period_units = "days";

    def spin(self) -> str:
        return "slightly eliptical";


class Comet(SolarObject):
    orbit_period_units = "years";

    def spin(self) -> str:
        return "spins like crazy";

if __name__ == "__main__":
    earth = Planet("Earth", 1, 365);
    mars = Planet("Mars", 1.4, 687);

    # Have to convert these to days since our base class uses days
    halley = Comet("Halley's Comet", 35, 76.95);
    halebopp = Comet("Hale-Bopp", 354, 2397.29);

    earth.display_solar_object();
    mars.display_solar_object();
    halley.display_solar_object();
    halebopp.display_solar_object();
