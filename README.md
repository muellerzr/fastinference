# fastinference
> A collection of inference modules for fastai2 including inference speedup and interpretability

# Contributors
[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/0)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/0)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/1)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/1)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/2)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/2)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/3)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/3)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/4)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/4)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/5)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/5)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/6)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/6)[![](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/images/7)](https://sourcerer.io/fame/muellerzr/muellerzr/fastinference/links/7)


## Install

`pip install fastinference`

## How to Help?

Do you have an interpretability method you love to use and want it integrated? Or do you see another way we can speed up `get_preds`, `predict`, etc? Go ahead and make a Pull Request with your feature!

Besides the directions [here](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) about how to make a GitHub PR, there's a few design rules:

We use [nbdev](https://github.com/fastai/nbdev) for development. What this means is we write the code out of notebooks and then make the library from them. Here are the steps to library development:

### Formatting:
Documentation from the code itself should be one line with a quick summary of what it's expecting, save the verbose for the notebook documentation. 

### Notebook -> Library
1. Make sure `nbdev` is installed
2. Write your code in the notebook, include the documentation in here as well (you can be as verbose as you want!) 
  > This notebook should be saved in the `nbs` folder with a number system (if it's unrelated to anything just do the next one up)
3. From your CLI of your choice run the following string of commands:
  1. `nbdev_build_lib`
  2. `nbdev_clean_nbs`
  3. `git add *`, etc
For our GitHub, we use GitHub actions to test our code before we merge any request automatically. You'll see a little green check mark if it was successful. Also **do not** run `nbdev_build_docs`. I will update the documentation every release

### Code -> Library
If you prefer coding in `.py` instead, that's fine too! Just a few different steps
1. Same as step 1 before
2. Write in your `.py` files inside the `fastinference` **subfolder** (where the rest of the `.py`'s are)
3. Run `nbdev_update_lib`
4. `git add *`, etc
* You (may) need to run `nbdev_clean_nbs` again but I do not believe so
