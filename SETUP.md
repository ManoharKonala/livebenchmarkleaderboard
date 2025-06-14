
# LLM Leaderboard Setup Guide

This guide will help you set up your GitHub repository to automatically update the LLM leaderboard every 12 hours.

## Step 1: Connect to GitHub

1. In Lovable, click the **GitHub** button in the top-right corner
2. Click "Connect to GitHub" and authorize the Lovable GitHub App
3. Select your GitHub account/organization
4. Click "Create Repository" to push your code to GitHub

## Step 2: Enable GitHub Actions

1. Go to your GitHub repository
2. Click on the **Settings** tab
3. In the left sidebar, click **Actions** → **General**
4. Under "Actions permissions", select **Allow all actions and reusable workflows**
5. Click **Save**

## Step 3: Verify the Workflow

1. Go to the **Actions** tab in your repository
2. You should see the "Update LLM Leaderboard" workflow
3. Click **Run workflow** to test it manually
4. The workflow will automatically run every 12 hours

## Step 4: Customize Data Sources (Optional)

The scraper currently uses curated real data. To fetch live data:

1. **Hugging Face Leaderboard**: 
   - The scraper attempts to fetch from the official HF leaderboard
   - You may need to adjust the parsing logic based on their HTML structure

2. **Chatbot Arena**:
   - Currently returns empty data
   - You can implement parsing for LMSYS Arena data

3. **Additional Sources**:
   - Add more benchmark sources in the `fetch_additional_benchmarks()` function

## Step 5: Monitor Updates

- Check the **Actions** tab for workflow runs
- The README will be automatically updated every 12 hours
- If a run fails, an issue will be created automatically

## Troubleshooting

- **Workflow not running**: Check that GitHub Actions are enabled
- **Permission errors**: Ensure the repository has proper write permissions
- **Scraping failures**: Check the workflow logs for specific error messages

## Manual Updates

You can manually trigger an update by:
1. Going to Actions → Update LLM Leaderboard
2. Clicking "Run workflow"
3. Selecting the main branch and clicking "Run workflow"

That's it! Your LLM leaderboard will now update automatically every 12 hours.

