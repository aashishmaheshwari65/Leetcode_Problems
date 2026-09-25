class Solution {
public:

    set<string> parse(string& s, int& i) {
        set<string> result;

        if (s[i] == '{') {
            i++; 

            while (true) {
    
                set<string> part = parse(s, i);


                result.insert(part.begin(), part.end());

                if (s[i] == ',') {
                    i++; 
                } 
                else if (s[i] == '}') {
                    i++; 
                    break;
                }
            }
        } 
        else {
   
            result.insert(string(1, s[i]));
            i++;
        }

        while (i < s.size() && s[i] != '}' && s[i] != ',') {
            set<string> next = parse(s, i);

            set<string> combined;

            for (const string& a : result) {
                for (const string& b : next) {
                    combined.insert(a + b);
                }
            }

            result = combined;
        }

        return result;
    }

    vector<string> braceExpansionII(string expression) {
        int i = 0;

        set<string> result = parse(expression, i);

        return vector<string>(result.begin(), result.end());
    }
};