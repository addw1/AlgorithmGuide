#include <assert.h>
#include <deque>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

class ChamberSecret {
private:
    vector<vector<int>> chamberMap;

public:
    void initMap(int n, int m, const string& s) {
        stringstream ss(s);
        string line;
        while (getline(ss, line, '\n')) {
            vector<int> row;
            stringstream streamLine(line);
            string word;
            while (streamLine >> word) {
                row.push_back(stoi(word));
            }
            chamberMap.push_back(row);
        }
        assert(chamberMap.size() == n && chamberMap[0].size() == m);
    }

    int getMinNum() {
        // cost map
        // [n, m, dir, cost]
        vector<vector<int>> costMap;
        costMap.resize(chamberMap.size());
        for(int i = 0; i < chamberMap.size(); i++) {
            costMap[i].resize(chamberMap[i].size());
        }

        for(int i = 0; i < chamberMap.size(); i++) {
            for(int j = 0; j < chamberMap[0].size(); j++) {
                    costMap[i][j] = -1;
            }
        }
        // init direction
        int fx[4] = {0, 0, -1, 1};
        int fy[4] = {-1, 1, 0, 0};
        int i = chamberMap.size() - 1;
        int j = chamberMap[0].size() - 1;
        int k = 2;
        costMap[i][j] = 0;
        // init the dequeue
        deque<int> q;
        q.push_front(k);
        q.push_front(j);
        q.push_front(i);
        while(!q.empty()) {
            // get the first element
            i = q.front();
            q.pop_front();
            j = q.front();
            q.pop_front();
            k = q.front();
            q.pop_front();
            int curCost = costMap[i][j];
            assert(curCost != -1);
            // find the adjacent elements which cost zero
            int nextI = i + fy[k];
            int nextJ = j + fx[k];
            int nextK = k;
            if(nextJ >= 0 && nextJ < costMap[0].size() && nextI >= 0 && nextI < costMap.size() &&  costMap[nextI][nextJ] == -1) {
                costMap[nextI][nextJ] = curCost;
                q.push_front(nextK);
                q.push_front(nextJ);
                q.push_front(nextI);
            }
            // find the adjacent element which cost 1
            if (chamberMap[i][j] == 1) {
                for (int tempK = 0; tempK < 4; tempK++) {
                    if (tempK == k) {
                        continue;
                    }
                    if(i + fy[tempK] >= 0 && i + fy[tempK] < chamberMap.size()
                    && j + fx[tempK] >= 0 && j + fx[tempK] < chamberMap[0].size()) {
                        if (costMap[i + fy[tempK]][j + fx[tempK]] != -1) continue;

                        costMap[i + fy[tempK]][j + fx[tempK]] = curCost + 1;
                        q.push_back(i + fy[tempK]);
                        q.push_back(j + fx[tempK]);
                        q.push_back(tempK);
                    }
                }
            }
        }
        return costMap[0][0];
    }
};
