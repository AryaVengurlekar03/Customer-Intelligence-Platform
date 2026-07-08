from src.analytics.dashboard_service import DashboardService


class KPIGenerator:

    def __init__(self):
        self.dashboard = DashboardService()

    def generate(self):

        print("\n========== KPI REPORT ==========\n")

        print(self.dashboard.get_total_revenue())

        print(self.dashboard.get_total_orders())

        print(self.dashboard.get_total_customers())

        print(self.dashboard.get_total_sellers())

        print("\n===============================\n")


if __name__ == "__main__":

    KPIGenerator().generate()