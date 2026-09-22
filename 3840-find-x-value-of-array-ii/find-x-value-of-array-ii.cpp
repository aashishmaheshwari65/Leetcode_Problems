class Solution {
public:
    int n, K;
    vector<int> prod, cnt;

    inline int& C(int p, int r) {
        return cnt[p * K + r];
    }

    void pull(int p) {
        int L = p << 1;
        int R = L | 1;

        prod[p] = (long long)prod[L] * prod[R] % K;

        int baseL = L * K;
        int baseR = R * K;
        int baseP = p * K;

        fill(cnt.begin() + baseP, cnt.begin() + baseP + K, 0);

        for (int r = 0; r < K; ++r)
            cnt[baseP + r] += cnt[baseL + r];

        for (int r = 0; r < K; ++r) {
            int nr = (long long)prod[L] * r % K;
            cnt[baseP + nr] += cnt[baseR + r];
        }
    }

    void build(int p, int l, int r, const vector<int>& nums) {
        if (l == r) {
            prod[p] = nums[l] % K;
            C(p, prod[p]) = 1;
            return;
        }

        int m = (l + r) >> 1;

        build(p << 1, l, m, nums);
        build(p << 1 | 1, m + 1, r, nums);

        pull(p);
    }

    void update(int p, int l, int r, int idx, int val) {
        if (l == r) {
            fill(cnt.begin() + p * K, cnt.begin() + p * K + K, 0);
            prod[p] = val % K;
            C(p, prod[p]) = 1;
            return;
        }

        int m = (l + r) >> 1;

        if (idx <= m)
            update(p << 1, l, m, idx, val);
        else
            update(p << 1 | 1, m + 1, r, idx, val);

        pull(p);
    }

    struct Info {
        int product;
        vector<int> cnt;
    };

    Info query(int p, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            Info res;
            res.product = prod[p];
            res.cnt.resize(K);

            int base = p * K;

            for (int i = 0; i < K; ++i)
                res.cnt[i] = cnt[base + i];

            return res;
        }

        int m = (l + r) >> 1;

        if (qr <= m)
            return query(p << 1, l, m, ql, qr);

        if (ql > m)
            return query(p << 1 | 1, m + 1, r, ql, qr);

        Info L = query(p << 1, l, m, ql, qr);
        Info R = query(p << 1 | 1, m + 1, r, ql, qr);

        Info res;
        res.product = (long long)L.product * R.product % K;
        res.cnt.assign(K, 0);

        for (int x = 0; x < K; ++x) {
            res.cnt[x] += L.cnt[x];

            int nx = (long long)L.product * x % K;
            res.cnt[nx] += R.cnt[x];
        }

        return res;
    }

    vector<int> resultArray(vector<int>& nums, int k,
                            vector<vector<int>>& queries) {
        n = nums.size();
        K = k;

        prod.assign(4 * n + 5, 1);
        cnt.assign((4 * n + 5) * K, 0);

        build(1, 0, n - 1, nums);

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto& q : queries) {
            int index = q[0];
            int value = q[1];
            int start = q[2];
            int x = q[3];

            update(1, 0, n - 1, index, value);

            Info res = query(1, 0, n - 1, start, n - 1);

            ans.push_back(res.cnt[x]);
        }

        return ans;
    }
};
