# API Testing — AI News Tracker

## 1. Objective

The purpose of this test was to explore and test the Hacker News Algolia Search API using Postman.

The API was tested to understand how news articles are retrieved, how the JSON response is structured, and which data fields will be needed for the AI News Tracker project.

## 2. API Request Configuration

| Property | Value |
|---|---|
| API provider | Hacker News Algolia |
| HTTP method | GET |
| Endpoint | https://hn.algolia.com/api/v1/search |
| Search query | AI |
| Tags | story |
| Results per page | 20 |
| Authentication | No authentication required for this test |

## 3. Test Results

| Test | Result |
|---|---|
| Request sent successfully | Yes |
| HTTP status | 200 OK |
| Response format | JSON |
| Articles returned (`hits.length`) | 20 |
| Total matching results (`nbHits`) | 2,033,713 |
| Pages reported (`nbPages`) | 50 |
| Current page | 0 |

## 4. JSON Response Structure

The API returned a JSON response containing information about the search results.

Important top-level fields:

| Field | Description |
|---|---|
| `hits` | Array containing the returned article objects |
| `hitsPerPage` | Maximum number of articles requested per page |
| `nbHits` | Total matching results reported by the API |
| `nbPages` | Number of pages reported by the API |
| `page` | Current page number |

## 5. Article Data Fields

The following fields will be inspected and used when processing individual articles:

| Field | Description | Data type |
|---|---|---|
| `objectID` | Unique article identifier | String |
| `title` | Article headline | String |
| `author` | Article submitter | String |
| `points` | Story points | Integer |
| `num_comments` | Number of comments | Integer |
| `url` | Original article URL | String |
| `created_at` | Article creation timestamp | String |

Note: Individual articles may contain missing or null values. These will need to be handled when processing the API response in Python.

## 6. Observations

- The API request was successful and returned HTTP status 200.
- The response was provided in JSON format.
- The request returned 20 article objects.
- The API reported 2,033,713 total matching results.
- The API uses pagination to divide search results into pages.
- The returned JSON structure provides the information needed to begin building the Python data retrieval component.

## 7. Conclusion

The initial API test was successful. Postman was used to send a GET request and inspect the JSON response.

The results provided an understanding of the API response structure and the article fields required for the project.

The next development stage will involve using Python to retrieve the same data programmatically and prepare it for storage in an SQLite database.

## 8. Evidence

Add screenshots of the following:

- [ ] Postman GET request configuration.
- [ ] Successful HTTP 200 response.
- [ ] JSON response showing the `hits` array and article fields.
- [ ] API results showing `nbHits`.