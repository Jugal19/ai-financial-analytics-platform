const API_BASE_URL = 'http://127.0.01:8000'

export async function fetchAnalyticsSummary()
{
    const res = await fetch(`${API_BASE_URL}/analytics/summary`)
    return res.json()
}

export async function fetchAnalyticsCategories()
{
    const res = await fetch(`${API_BASE_URL}/analytics/categories`)
    return res.json()
}

export async function fetchAnalyticsTrends()
{
    const res = await fetch(`${API_BASE_URL}/analytics/trends`)
    return res.json()
}