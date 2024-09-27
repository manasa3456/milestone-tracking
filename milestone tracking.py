class Milestone:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️ Completed" if self.completed else "❌ In Progress"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


class MilestoneTracker:
    def __init__(self):
        self.milestones = []

    def add_milestone(self, title, description, due_date):
        milestone = Milestone(title, description, due_date)
        self.milestones.append(milestone)
        print(f"Added milestone: {title}")

    def complete_milestone(self, title):
        for milestone in self.milestones:
            if milestone.title == title:
                milestone.mark_completed()
                print(f"Marked milestone '{title}' as completed.")
                return
        print(f"Milestone '{title}' not found.")

    def view_milestones(self):
        if not self.milestones:
            print("No milestones to display.")
            return
        for milestone in self.milestones:
            print(milestone)


def main():
    tracker = MilestoneTracker()

    while True:
        print("\nMilestone Tracker")
        print("1. Add Milestone")
        print("2. Complete Milestone")
        print("3. View Milestones")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            title = input("Enter milestone title: ")
            description = input("Enter milestone description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            tracker.add_milestone(title, description, due_date)

        elif choice == '2':
            title = input("Enter the title of the milestone to complete: ")
            tracker.complete_milestone(title)

        elif choice == '3':
            tracker.view_milestones()

        elif choice == '4':
            print("Exiting Milestone Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
