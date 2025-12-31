<template>
    <div class="max-w-7x1 mx-auto space-y-6">
        <div class="space-y-6">
            <!-- Page Header -->
            <div>
                <h2 class="text-2xl font-bold">Analytics</h2>
                <p class="text-gray-400 text-sm">Financial trends and breakdowns</p>
            </div>

            <!-- KPI Section-->
            <div v-if="isLoading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div v-for="i in 4" :key="i" class="h-24 bg-gray-800 rounded-xl animate-pulse"/>
            </div>

            <div v-else-if="!hasData" class="bg-gray-900 border border-gray-800 rounded-xl p-8 text-center text-gray-400">
                <AnalyticsKPI label="Total Income" value="$0.00" />
                <AnalyticsKPI label="Total Expenses" value="$0.00" />
                <AnalyticsKPI label="Net Savings" value="$0.00" />
                <AnalyticsKPI label="Average Monthly Spend" value="$0.00" />
            </div>

            <!-- Main Analytics Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                
                <!-- Trend Chart Placeholder -->
                <div class="lg:col-span-2 bg-gray-900 border border-gray-800 rounded-xl p-6">
                    <h3 class="text-lg font-semibold mb-4">Spending Over Time</h3>
                </div>

                <div class="h-64 flex items-center justify-center text-gray-500 text-sm border border-dashed border-gray-700 rounded-lg">
                    Analytics chart will appear once data is available
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
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import AnalyticsKPI from '../components/AnalyticsKPI.vue'

    const isLoading = ref(false)
    const hasData = ref(false)
</script>