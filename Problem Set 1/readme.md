# pset1

You just bought a parcel of land that is K kilometers long; it is so narrow that, for the purposes of this problem, we will consider it to be a polyline that runs from west to east, varying in elevation. You know the elevations of the land (in meters) at K + 1 regularly spaced measurement marks M0, M1, ..., MK. These marks are 0, 1, ..., K km, respectively, from the western end.

In this region, a wooden post denotes the boundary between two adjacent parcels of land. Wooden posts can only be placed at measurement marks, and there can be at most one post at each mark. Right now, there are two posts: one at the 0 km mark, and one at the K km mark. A measurement mark with a post is considered to be part of both of the parcels it demarcates, so your parcel of land includes all measurement marks between 0 and K km, inclusive.

A parcel is considered desirable if it contains three measurement marks such that the west-most and east-most of those three marks are both strictly higher than the remaining one of the three marks, or both strictly lower than the remaining one of the three marks. People like some variation in their landscapes! Notice that these three marks are not necessarily consecutive, and the west-most and east-most of the three marks are not necessarily the west-most and east-most marks of the parcel.

Consider an example with K = 5 and M0, M1, ..., MK = 5, 6, 6, 1, 2, 4. The measurement marks with elevations 5, 2, and 4 satisfy the condition, as do the measurement marks with elevations 6, 1, and 2. However, the measurement marks with elevations 6, 6, and 1 do not satisfy the condition, nor do the measurement marks with elevations 1, 2, and 4. Any three measurement marks that satisfy the condition make the whole parcel desirable; for example, a parcel containing the measurement marks 4 7 6 7 is desirable because of the first three values.

Your parcel is desirable, but you think it may be possible to extract even more value from it! You want to add additional posts to this parcel to divide it up into multiple parcels, all of which must be desirable, since you do not want to waste any land. What is the largest number of posts you can add?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with one line containing an integer K: the length, in kilometers, of your parcel of land. Then, there is one more line with K + 1 integers M0, M1, ..., Mk; where Mi is the elevation (in meters) at the measurement mark that is i km from the western end of your land.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the largest possible number of posts you can add, as described above.

Limits
Time limit: 20 seconds per test set. (10 seconds per test run.)
Memory limit: 1GB.
1 ≤ T ≤ 100.
0 ≤ Mi ≤ 1000, for all i.
(Mi - Mj) × (Mk - Mj) > 0, for some i < j < k. (Your starting parcel is desirable.)

Test set 1 (Visible)
4 ≤ K ≤ 10.

Test set 2 (Hidden)
4 ≤ K ≤ 1000.

Sample

Input

Output

4

4

4 8 7 3 5

4

4 8 7 7 5

7

1 2 2 1 2 1 2 1

6

2 1 3 10 9 12 20


Case #1: 1

Case #2: 0

Case #3: 2

Case #4: 1

In Sample Case #1, you can add one post at 2 km to get a total of two desirable parcels. The parcel from 0 to 2 km is desirable because 4 < 8 and 8 > 7. The parcel from 2 to 4 km is desirable because 7 > 3 and 3 < 5.

In Sample Case #2, there is no way to add another post. If you added one at 1 km or 3 km, one of the parcels would include only two measurement marks and could not be desirable. If you added one at 2 km, the parcel between 0 and 2 km would be desirable, but the parcel between 2 and 4 km would not.

In Sample Case #3, posts can be added at 3 km and 5 km.

In Sample Case #4, a post can be added at 2 km. Notice that the parcel from 2 km to 6 km is desirable because 10 > 9 and 9 < 12. However, there is no way to add a second post.
