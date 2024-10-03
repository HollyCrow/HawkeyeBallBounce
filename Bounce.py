import numpy as np


# I am unconvinced by the use of a class for this,
# but for readabilities sake I think it is likely a the preferable option.
# TODO: further comment the values in this class.
class Bounce:
    # --- Varibles from dataset: ---

    #overNumber = 0                 # Over number, unused.
    #ballNumber = 0                 # Ball number, unused.
    #bowlerName = ""                # Bowler name, Unused.
    #batsmansHand = True            # Hand used, Unused. True for right, False for left.
    bowlerReleaseSpeed = 0.0  # float

    # Note: All variables with "Pos" and compressions of their corresponding 1D values in the dataset.
    # Dimensions will be spesified next to them respectively.
    # Acceleration also follows this rule.
    bouncePos = np.array([0.0, 0.0])  # X,Y
    stumpsPos = np.array([0.0, 0.0])  # Y,Z
    swing = 0.0
    deviation = 0.0
    #runsScored = NaN               # Unused(?)
    shotLandingPos = np.array([0.0, 0.0])  # X,Y
    #trajectoryTime = 0             # Unused. Should not be a number?
    #trajectoryDate = 0             # Unused. Also not a number.
    bounceVelocity = 0.0  # Bounce velocity.
    outOfBounceAngle = 0.0
    dropAngle = 0.0
    angleLeavingBowlersHand = 0.0  # Come up with better variable names istg.
    #shotPlayed = ""                # Unused.
    #shotType = ""                  # Unused.
    bowlerReleasePos = np.array([0.0, 0.0])  # Yposition,Zposition (Pick a the damn naming scheme)
    acceleration = np.array([0.0, 0.0])  #Y,Z

    # --- ---

    # Not sure if this is the intended use of __repr__()?
    def __repr__(self):
        name = (f"bowlerReleaseSpeed: {self.bowlerReleaseSpeed}\n"
                f"bouncePos: {self.bouncePos}\n"
                f"stumpsPos: {self.stumpsPos}\n"
                f"swing:{self.swing}\n"
                f"deviation: {self.deviation}\n"
                f"shotLandingPos: {self.shotLandingPos}\n"
                f"bounceVelocity: {self.bounceVelocity}\n"
                f"outOfBounceAngle: {self.outOfBounceAngle}\n"
                f"dropAngle: {self.dropAngle}\n"
                f"angleLeavingBowlersHand: {self.angleLeavingBowlersHand}\n"
                f"bowlerReleasePos: {self.bowlerReleasePos}\n"
                f"acceleration: {self.acceleration}")

        return name
