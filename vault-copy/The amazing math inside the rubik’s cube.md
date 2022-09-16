---
author: ohmanfoo
created: '2022-09-15'
source: '#todo'
tags: '#1997 #1981 #June #2005 #representative #1990 #corn #1980 #mental #1974 #Breaking
  #2010 #2000 #trade #1982 #white #experiment #ABC #1576 #1633 #1674 #1862 #1930 #1966 '
title: The amazing math inside the rubik’s cube
---

# The Amazing Math Inside the Rubik’s Cube

> ## Excerpt
> Want to solve the puzzle? Then you have to know the numbers.

---
![puzzle against black backdrop](https://pocket-syndicated-images.s3.amazonaws.com/6105b61d8cd57.png)

Photo by  Andrew Spencer/Getty Images

Ever since the Rubik’s Cube was released, it’s taunted almost a half billion tinkerers who think they can crack its confounding mysteries, only to be stymied by its maddening secrets. Now, it’s time to unpack the puzzle once and for all—using some deep math. The cube’s literal insides are made of plastic, but its real guts are nothing but numbers. Let’s dive in.

![dog eyeing puzzle](https://pocket-image-cache.com/direct?resize=w[[2000]]&url=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod.s3.amazonaws.com%2Fimages%2Fgallery-shoot-date-september-13-[[1982]]-leo-the-dog-as-jack-news-photo-[[1576]]5[[1674]]2.jpg%3Fresize%3D480%3A%2A)

Photo by [[ABC]] Photo Archives/Getty Images

___

### [[Breaking]] Apart the Blocks

Starting with some basics, a 3x3x3 Rubik’s Cube has six faces, each a different color. The center of each face is attached to the core scaffold that holds the cube together, so they don’t move other than rotating in place. As a result, the same colors always end up opposite from each other; on a standard cube, [[white]] is opposite yellow, red opposite orange, and blue opposite green.

Bust open a Rubik’s Cube and you’ll see it’s made of three types of building blocks. First, there’s that central scaffold, connecting the center of each face. Then there are the cubies—the nickname for the little 1x1x1 blocks. The [[corn]]er cubies have three colored sides, and the edge cubies have two. A Rubik’s Cube has one core, eight [[corn]]er cubies, and 12 edge cubies.

![blocks of a cube](https://pocket-image-cache.com/direct?resize=w[[2000]]&url=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod.s3.amazonaws.com%2Fimages%2Frubiks-inside-[[1576]]5[[1633]]8.jpg%3Fresize%3D480%3A%2A)

Photo by Creative Commons/Wikivisual

The immediate math to be done with those numbers is the total number of ways you can scramble a Rubik’s cube: 43,252,003,274,489,856,000. Written in a more mathematical way, that number is (3_8_8!)(21212!)/12. Here’s how that comes together.

The first term, 38, counts every way the eight-[[corn]]er cubies can be rotated. A [[corn]]er cubie can fit into its slot rotated three different ways. That’s a factor of 3 for each of the eight [[corn]]er cubies, so they multiply to 38.

Next is where each [[corn]]er cubie goes. There are eight [[corn]]er slots, so the first [[corn]]er cubie has eight options. The second [[corn]]er cubie is left with seven options, the next left with six, and so on, down to the last [[corn]]er cubie, which must go in the last [[corn]]er slot. That yields the calculation 8\*7\*6\*5\*4\*3\*2\*1, which is 8!, or “eight factorial.”

Thus the first chunk, (388!), counts every way the [[corn]]er cubies can fit into the cube. The 38 is their orientations, while the 8! is their locations.

The next chunk, (21212!), is the same idea, now for the edges. Edges only have two orientations, so the 12 of them have a total of 212 mixes of orientations. Then there are 12 locations, so 12! is the number of ways they can go to those spots.

What’s left of the formula (388!)(21212!)/12 is that division by 12. It relates to a fact about Rubik’s Cube that is often felt, but not always understood. Here’s a thought [[experiment]] (which perhaps you’ve done for real!) to illustrate:

Suppose you break open a Rubik’s Cube, remove each cubie, and then put all the cubies back in random slots (with [[corn]]er cubies only fitting in the [[corn]]ers, and edge cubies only in the edges). You get what looks like a normal scrambled cube, and so far we’ve counted every way you could do this, (388!)(21212!). Now, is it always possible to solve this jumbled cube, without breaking it apart?

The answer is no.

This is a trap that has caught many novice cubers. If you’re practicing and you want to scramble a solved cube, you have to keep the cube intact and scramble it up manually. If you break it apart and reassemble the cubies randomly, there’s actually only a 1 in 12 chance that it’s solvable.

___

### The Answer’s in the Algorithms

Want to understand why that’s 1 in 12? Well, there’s a nice visual way to get a sense of it. A cube that’s been broken and reassembled with its cubies randomly scrambled will have equal chances of being solvable to one of the following [[representative]]s.

![puzzles in rows](https://pocket-image-cache.com/direct?resize=w[[2000]]&url=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod.s3.amazonaws.com%2Fimages%2Frubiks-equivalences-classes-[[1576]]5[[1862]]3.png%3Fresize%3D480%3A%2A)

The orange, yellow, and green sides. Photo by Dave Linkletter

We’ve arranged these to splay out the different factors leading to 12. Row 1 has normal [[corn]]ers. Rows 2 and 3 have one [[corn]]er rotated in place. Column 1 has normal edges. Column 2 has one edge flipped in place. Column 3 has two edges swapped. Finally, column 4 has one edge flipped plus two edges swapped.

So the 12 cubes in the photo above can’t be transformed into one another. And there’s no 13th arrangement that can’t transform into one of those 12. How do we know this?

There’s a connection here with what can and can’t be done by moving the cube’s faces. A sequence of moves is often referred to as an “algorithm” by cube enthusiasts. The sought-after algorithms are those that move just a few of the cubies while leaving the rest untouched. The limitations to the algorithms are the key to that number 12.

That 12 comes together from three factors getting multiplied: 12 = 3\*2\*2. We need to grapple with a factor of 3, and two factors of 2.

The factor of 3 comes down to this: There’s an algorithm that twists each of two different [[corn]]ers, but there’s _no_ algorithm that twists a single [[corn]]er (while leaving everything else unmoved). So if you grab a normal Rubik’s Cube, pry out a single [[corn]]er, and replace it twisted, it becomes impossible to solve, and you’ll have moved from the top-left [[corn]]er of our chart to one of the spots right below it.

However, if you repeat that process, and twist one more [[corn]]er, it doesn’t add a second factor of 3. Now that two [[corn]]ers are twisted, we can apply the algorithm that twists two [[corn]]ers, until at least one is fixed. If the other one happens to get fixed in the process, we got lucky and now we’re back to a solvable cube. Overall, the [[corn]]ers’ orientations can go one of three ways.

![baby solving a puzzle](https://pocket-image-cache.com/direct?resize=w[[2000]]&url=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod.s3.amazonaws.com%2Fimages%2Fbaby-lies-in-bed-holding-a-rubiks-cube-circa-[[1981]]-news-photo-[[1576]]5[[1930]]5.jpg%3Fcrop%3D0.905xw%3A0.833xh%3B0.0138xw%2C0.147xh%26resize%3D480%3A%2A)

Photo by Hulton Archive/Getty Images

The first factor of 2 is similar. There’s an algorithm that flips, in place, each of two different edges, but no algorithm can flip a single edge in place. So any number of flipped edges can be shimmied down to a single edge, which winds up either flipped or not, for two possibilities.

The last factor of 2 actually involves edges and [[corn]]ers, though we showed it on the chart with edges. There’s an algorithm that swaps two [[corn]]ers while also swapping two edges. There aren’t any algorithms that can swap only a pair of [[corn]]ers, nor only a pair of edges.

If you have a cube, pry out two edges, and swap them, you jump by two columns on our chart—either between columns 1 and 3, or between 2 and 4. The same is true if you swap a pair of [[corn]]ers. But swapping a pair of edges _and_ a pair of [[corn]]ers cancel each other out, since there’s an algorithm to undo that.

___

### The _Pop Mech_ Rubik’s Cube Proof

Now, if you’re thinking inquisitively, you could desire proof for some of the claims in the last paragraphs. Is there some deeper math that can prove “there’s no algorithm that flips one edge cubie in place without moving any other cubie”? You bet. Here’s how that mathematical proof roughly goes:

> When a face of the cube is turned, four edge cubies get moved. Consider, for instance, an algorithm of 10 moves. For each cubie, follow it through the algorithm, and count how many times it gets moved, and call that its cubie-moves count. Add up those numbers for every edge cubie, and the total must come to 40 cubie-moves, since each of the 10 moves adds four to the total.

> In general, any algorithm’s total number of cubie-moves for the edge cubies must be a multiple of 4. Now for a critical pair of facts: If an edge cubie is moved an even number of times and returned back to the same slot, it will have the same orientation. Conversely, if an edge cubie is moved an odd number of times and put back in the same slot, it will be flipped.

> And yes, that pair of facts can be proven with _even deeper_ math, but we’ll stop zooming in from here, in the name of this article eventually ending. You can also check the two facts experi[[mental]]ly and get a feel for why they’re true. (For this proof, a 180-degree turn counts as two moves of each cubie involved.)

> Finally, consider a hypothetical algorithm that accomplishes the goal here, flipping one edge cubie in place without changing any other cubie. The one flipped edge was therefore moved an odd number of times by the algorithm, while each of the other 11 edges was moved an even number of times. The sum of 11 even numbers and one odd number is always odd, but we established earlier that this sum must be a multiple of 4. An odd number is a multiple of 4? That’s impossible. Therefore no such algorithm exists.

You’ve now explored (388!)(21212!)/12, the number of cube configurations, which, to a mathematician studying the cube, is just preliminary. To go deeper into the math, you might wonder a common meta-question: “Are there any unanswered math questions in this subject?”

![man solving a puzzle](https://pocket-image-cache.com/direct?resize=w[[2000]]&url=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod.s3.amazonaws.com%2Fimages%2Fhungarian-contestant-zoltanh-labas-competes-in-the-first-news-photo-[[1576]]5[[1966]]3.jpg%3Fcrop%3D0.972xw%3A0.961xh%3B0.00864xw%2C0.0244xh%26resize%3D480%3A%2A)

Photo by Pictorial Parade/Getty Images

___

### **God’s Number and Beyond**

The original challenge of the cube, of course, was solving it. Ernő Rubik made his first prototype in [[1974]], and early in the six years it took him to see it mass-produced, he was naturally the first person to ever solve the cube.

When the cube hit toy stores in [[1980]], some mathematicians had already been [[experiment]]ing with early versions for a few years. One of them was Dr. David Singmaster, who wrote the famous guide “Notes on Rubik’s ‘Magic Cube’” and developed a writing method for describing turns of the cube’s faces. That notation has become the standard, and is now known as Singmaster notation.

If this were an article in the [[1980]]s, the labor of explaining Singmaster notation, and using it to guide you through the algorithms of solving the cube, might be worth it. Plenty of articles did just that. But now [Youtube tutorials exist](https://www.youtube.com/results?search_query=how+to+solve+a+rubik%27s+cube), so that practice is obsolete.

The fastest solution times for Rubik’s Cube steadily crept down over the decades. The world record by a human is currently [3.47 seconds](https://www.youtube.com/watch?v=cm5vp4z5l5Y). Instru[[mental]] to this era of speed cubing was Dr. Jessica Fridrich, who in [[1997]] developed a method for solving the cube faster than ever. Most of the fastest cube solvers nowadays use some version of the Fridrich method.

As some people sharpened their dexterity, others honed in on the ultimate math questions of Rubik’s Cube. No matter how scrambled a cube gets, how few moves can be applied to solve it? If someone scrambled your cube using 500 moves, it’s certainly possible to unscramble it in fewer than 500 moves. But how many fewer?

Thus, the pinnacle of the math in this subject was identified: Is there a magic number that allows us to say, “every scrambled cube can be solved in this many moves \[or less\]”? Thanks to early quips about divine intervention being necessary to glean it with confidence, that number became known as “God’s number.”

The first major insight on God’s Number was by Dr. Morwen Thistlethwaite in [[1981]], who proved it was at most 52. That means he proved every scrambled cube can be solved in 52 moves or less.

Progress continued through the [[1990]]s and [[2000]]s. Finally, in [[June]] [[2010]], a team of four scientists proved that [God’s number is 20](http://www.cube20.org/). That website, which the scientists have maintained ever since, contains the most advanced knowledge about Rubik’s cube to date.

So no matter how scrambled a Rubik’s Cube looks, it’s always 20 moves away from solved.

Only small tidbits of math remain unresolved for Rubik’s Cube. While God’s number is 20, it’s unknown exactly how many of the 43,252,003,274,489,856,000 combinations require a whole 20 moves to be solved.

The number of positions that require exactly one move to be solved is 18. That’s easy to calculate: There are six faces and three ways to twist each one. How many cubes are exactly two or three moves from solved isn’t tough for mathematicians to calculate, but you can imagine the higher numbers get tricky. The current knowledge goes up to 15; we know exactly how many positions are 15 moves from solved, but not precisely how many for 16 through 20 moves.

And that’s the last math question for the Rubik’s Cube. Now you’re all caught up until someone answers it. We’ll let you know when we do.

![robot working on a puzzle](https://pocket-image-cache.com/direct?resize=w[[2000]]&url=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod.s3.amazonaws.com%2Fimages%2Frobot-attempts-to-solve-a-rubiks-cube-at-the-[[trade]]-fair-news-photo-[[1576]]5[[2005]]5.jpg%3Fresize%3D480%3A%2A)

Photo by DAVID HECKER/Getty Images