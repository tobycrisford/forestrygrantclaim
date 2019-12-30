# forestrygrantclaim
Tool for finding the optimum grant claim for a new forest


When claiming a grant for planting a forest, there are different payment rates for different forest types.
For a forest to qualify as a particular type it must meet a number of constraints (e.g. maximum percentage conifer in a Native Broadleaf woodland).
However, given a forest plan, you can divide it up into multiple areas of different types instead of putting the whole area under the same claim.
What's more, the parts of a forest being allocated to a particular type need not be joined together.
You can allocate an area in one corner of your forest, and an area in another corner, to Native Broadleaf, if they meet the constraints when taken together, even if neither meets the constraints when taken alone.

The above points mean that maximizing the grant (given a forest plan) is a linear programming problem, with the number of hectares of each tree species in your plan as inputs. The geographical arrangement is essentially irrelevant.

This python script finds the maximum grant.

Current values and schemes in the script are just a demonstration. It needs to be modified before use.
