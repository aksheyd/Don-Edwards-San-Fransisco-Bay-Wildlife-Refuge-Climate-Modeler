#include <iostream>
#include <string>
#include <stdio.h>
#include <cstdlib>
#include <chrono>
#include <thread>

using namespace std;

void command_screen();
void DESFB_overview();
void modeler_main();
void instructions();
void change_climate(int input);

int main() {
    int input;

    system("clear && printf \'\\e[3J\'");
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
    system("clear && printf \'\\e[3J\'");
    string input;

    cout << "Don Edwards San Francisco Bay National Wildlife Refuge, CA, USA" << endl;
    cout << "===============================================================" << endl << endl;

    cout << "Habitats: Marsh, Ponds, Mudflat, Vernal Pools, Uplands" << endl;
    cout << "Species: 269 Birds, 28 Mammals, 12 Amphibian/Reptiles, 62 Fish, 335 Fauna" << endl;
    cout << endl;

    
    std::this_thread::sleep_for(chrono::nanoseconds(10));
    std::this_thread::sleep_until(std::chrono::system_clock::now() + std::chrono::seconds(1));
    system("clear && printf \'\\e[3J\'");
    

    cout << "Here's a sneakpeek at some of the birds, mammals, etc" << endl;
    cout << "For the Danger Level coloumn, this number is calculated based on the inital data given" << endl <<
            "from the US Fish & Wildlife Service. It is based on many factors including the species" << endl <<
            "origin, endangered-level, etc." << endl;
    
    std::this_thread::sleep_for(chrono::nanoseconds(10));
    std::this_thread::sleep_until(std::chrono::system_clock::now() + std::chrono::seconds(1));
    

    string filename = "\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/sheet_analyzer.py\"";
    string command = "python3 ";
    command += filename + " -p 60"; //accounts for command line arguements
    system("clear && printf \'\\e[3J\'");
    system(command.c_str());

    filename = "\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/print_data.py\"";
    command = "python3 ";
    command += filename;
    system("clear && printf \'\\e[3J\'");
    system(command.c_str());

    cout << "Please click enter when you are ready to move on!" << endl;
    cin >> input;

    modeler_main();
    return;
}

void modeler_main() {
    system("clear && printf \'\\e[3J\'");

    int input;
    cout << "Now, it\'s your turn! Use the following instructions to affect the climate:" << endl << endl;
    instructions();
    cin >> input;

    while (input < 0 || input > 99) {
        cout << "Error: incorrect input detected." << endl;
        instructions();
        cin >> input;
    }

    change_climate(input);
    return;
}

void instructions() {
    // Make this a more robust command system, for now its just the desired temperature
    cout << "Input a temperature from 0 to 99 degrees Fahrenheit." << endl;
    cout << "Ex: 50, 95, 99, 5, etc." << endl;
}

void change_climate(int input) {
    string inp_s = to_string(input);
    string filename = "\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/sheet_analyzer.py\"";
    string command = "python3 ";
    command += filename + " -p " + inp_s; //accounts for command line arguements
    cout << command << endl;
    system("clear && printf \'\\e[3J\'");
    system(command.c_str());

    filename = "\"/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/print_data.py\"";
    command = "python3 ";
    command += filename;
    system("clear && printf \'\\e[3J\'");
    system(command.c_str());
    

    int hel;
    cin >> hel;
}