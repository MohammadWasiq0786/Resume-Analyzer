from fastmcp import FastMCP
from app import fetch_linkedin_jobs,fetch_naukri_jobs



mcp = FastMCP("fetch job")


@mcp.tool()
def fetchnaukri(listofkey):
    return fetch_naukri_jobs(listofkey)

@mcp.tool()
def fetchlinkedin(listofkey):
    return fetch_linkedin_jobs(listofkey)

if __name__ == "__main__":
    mcp.run()