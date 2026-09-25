class Solution 
{
public:
    int reverse(int x) 
    {

        long reverse_number = 0;
        long long int int_max = pow(2,31) - 1;
        long long int int_min = -(pow(2,31));

        while(x!=0)
        {
            int mod_number = x % 10;
            reverse_number = reverse_number * 10 + mod_number;

            x = x/10;
        }

        if(reverse_number > int_max || reverse_number < int_min){
            return 0;
        }

        return reverse_number;
    }
};