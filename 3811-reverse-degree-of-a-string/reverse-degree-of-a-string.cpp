class Solution {
public:
    int reverseDegree(string s) {
        
        int total_degree = 0;

        std:: vector<char> chars(s.begin(),s.end());
        
        for (int i=0; i<s.length(); i++)
            {
                int x = 26 - (chars[i] - 'a') ;              
                total_degree += x*(i+1) ;
            }    

        return total_degree;
    }
};