<template>
    <div class="space-y-6">
        <!-- Page Header -->
        <div>
            <h2 class="text-2xl font-bold">Analytics</h2>
            <p class="text-gray-400 text-sm">Financial trends and breakdowns</p>
        </div>

        <!-- KPI Section-->
        <div class="grid grid-cols01 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <AnalyticsKPI label="Total Income" value="$0.00" subtitle="This period" />

            <AnalyticsKPI label="Total Expenses" value="$0.00" subtitle="This period" />

            <AnalyticsKPI label="Net Savings" value="$0.00" subtitle="Income - Expenses" />

            <AnalyticsKPI label="Avg Monthly Spend" value="$0.00" subtitle="Rolling Average" />
        </div>

        <!-- Main Analytics Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            <!-- Trend Chart Placeholder -->
            <div class="lg:col-span-2 bg-gray-900 border border-gray-800 rounded-xl p-6">
                <h3 class="text-lg font-semibold mb-4">Spending Over Time</h3>
            </div>

            <div class="h-64 flex items-center justify-center text-gray-500 text-sm border border-dashed">
                Time-series chart will render here
            </div>
        </div>

        <!-- Category Breakdown -->
        <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
            <h3 class="text-lg font-semibold mb-4">Category Breakdown</h3>

            <ul class="space-y-3 text-sm text-gray-400">
                <li class="flex justify-between">
                    <span>Groceries</span>
                    <span>$0.00</span>
                </li>

                <li class="flex justify-between">
                    <span>Rent</span>
                    <span>$0.00</span>
                </li>

                <li class="flex justify-between">
                    <span>Other</span>
                    <span>$0.00</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
    import AnalyticsKPI from '../components/AnalyticsKPI.vue'
</script>