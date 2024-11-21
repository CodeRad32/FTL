#include <iostream>
#include <cmath>

using namespace std;

const double GRAVITATIONAL_CONSTANT = 6.67430e-11; // m^3 kg^-1 s^-2
const double MASS_OF_THE_UNIVERSE = 3.0e42; // kg (approximate)
const double SPEED_OF_LIGHT = 299792458.0; // m/s

int main() {
    double spacecraftMass = 1000.0; // kg (approximate mass of a spacecraft)
    double initialVelocity = 0.0; // m/s (initial velocity of the spacecraft)
    double timeStep = 1.0; // s (time step for simulation)

    double distanceFromCenter = 0.0; // m (distance from the center of the universe)
    double velocity = initialVelocity; // m/s (velocity of the spacecraft)

    cout << "Escape velocity from the universe: " << sqrt(2 * GRAVITATIONAL_CONSTANT * MASS_OF_THE_UNIVERSE / spacecraftMass) << " m/s" << endl;

    while (true) {
        // Calculate the acceleration due to gravity
        double acceleration = -GRAVITATIONAL_CONSTANT * MASS_OF_THE_UNIVERSE / pow(distanceFromCenter + MASS_OF_THE_UNIVERSE, 2);

        // Update the velocity and position
        velocity += acceleration * timeStep;
        distanceFromCenter += velocity * timeStep;

        // Check if we've reached the edge of the universe
        if (distanceFromCenter > MASS_OF_THE_UNIVERSE) {
            cout << "We've reached the edge of the universe! Velocity: " << velocity << " m/s" << endl;
            break;
        }

        // Check if we've reached escape velocity
        if (velocity > sqrt(2 * GRAVITATIONAL_CONSTANT * MASS_OF_THE_UNIVERSE / spacecraftMass)) {
            cout << "We've reached escape velocity! Velocity: " << velocity << " m/s" << endl;
            break;
        }

        // Print the current state
        cout << "Time: " << distanceFromCenter / velocity << " s" << endl;
        cout << "Distance from center: " << distanceFromCenter << " m" << endl;
        cout << "Velocity: " << velocity << " m/s" << endl;
        cout << endl;
    }

    return 0;
}
