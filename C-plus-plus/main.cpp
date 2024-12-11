#include <iostream>
#include "./graph/ChamberSecret.hpp"
int main() {
    ChamberSecret chamberSecret;
    chamberSecret.initMap(3, 3, "0 1 0\n0 0 0\n0 1 0");
    cout <<  chamberSecret.getMinNum() << endl;
    return 0;
}
