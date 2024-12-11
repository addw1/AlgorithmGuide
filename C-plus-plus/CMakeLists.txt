cmake_minimum_required(VERSION 3.29)
project(C_plus_plus)

set(CMAKE_CXX_STANDARD 11)

add_executable(C_plus_plus main.cpp
        graph/graphStoreEdge.cpp
        graph/ChamberSecret.hpp)
