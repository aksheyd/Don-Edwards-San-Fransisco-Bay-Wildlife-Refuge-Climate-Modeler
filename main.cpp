#include <iostream>
#include <string>
#include <stdio.h>
#include <cstdlib>

//#include <boost/python.hpp>

using namespace std;

void command_screen();
void DESFB_overview();

int main() {
    int input;

    system("clear");
    cout << "Welcome to the Don Edwards San Fransisco Bay Wildlife Refuge Climate Modeler" << endl;
    cout << "Please choose an option from below:" << endl;
    cout << "1: Start" << endl;
    cout << "2: Quit" << endl;

    while (cin >> input) {
        if (input == 1) {
            DESFB_overview();
            break;
        } else if (input == 2) {
            break;
        } else {
            command_screen();
        }
    }
    return 0;
}

void command_screen() {
    cout << "Incorrect input selected, please try again:" << endl;
    cout << "1: Start" << endl;
    cout << "2: Quit" << endl;
}

void DESFB_overview() {
    system("clear");
    int input;

    cout << "Don Edwards San Francisco Bay National Wildlife Refuge, CA, USA" << endl;
    cout << "===============================================================" << endl << endl;

    cout << "Habitats: Marsh, Ponds, Mudflat, Vernal Pools, Uplands" << endl;
    cout << "Species: 269 Birds, 28 Mammals, 12 Amphibian/Reptiles, 62 Fish, 335 Fauna" << endl;
    cout << "Data From US Fish & Wildlife Services: https://fws.gov/refuge/Don_Edwards_San_Francisco_Bay/" << endl;

    system("\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/run_python.sh\"");

    cout << "E: Endangered; T: Threatened; SSC: State Species of Concern" << endl;
    cin >> input;
}