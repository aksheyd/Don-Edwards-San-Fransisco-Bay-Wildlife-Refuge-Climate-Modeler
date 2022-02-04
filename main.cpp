#include <iostream>
#include <string>
#include <stdio.h>
#include <cstdlib>
#include <chrono>
#include <thread>

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
    cout << endl;

    /*
    std::this_thread::sleep_for(chrono::nanoseconds(10));
    std::this_thread::sleep_until(std::chrono::system_clock::now() + std::chrono::seconds(15));
    system("clear");
    */

    cout << "Here's a sneakpeek at some of the birds, mammals, etc" << endl;
    cout << "For the Danger Level coloumn, this number is calculated based on the inital data given" << endl <<
            "from the US Fish & Wildlife Service. It is based on many factors including the species" << endl <<
            "origin, endangered-level, etc." << endl;
    /*
    std::this_thread::sleep_for(chrono::nanoseconds(10));
    std::this_thread::sleep_until(std::chrono::system_clock::now() + std::chrono::seconds(4));
    */

    string filename = "\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/sheet_analyzer.py\"";
    string command = "python3 ";
    command += filename;
    system("clear");
    system(command.c_str());

    filename = "\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/print_data.py\"";
    command = "python3 ";
    command += filename;
    system("clear");
    system(command.c_str());

    cin >> input;
}