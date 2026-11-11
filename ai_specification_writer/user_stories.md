# Carpool Connect — User Stories

This document defines user stories for **Carpool Connect**, a carpooling platform that matches drivers and passengers with similar routes and schedules. It supports individuals as well as organizations such as companies and universities.

## User Stories

### User Story 1: Create an Account
As a driver or passenger, I want to create an account so that I can use Carpool Connect with a personal profile.

**Acceptance Criteria**:
- A user can register with a valid email address and password.
- The system validates required fields and displays clear errors for invalid or duplicate details.
- A user can sign in after successful registration.

**Priority**: MVP

### User Story 2: Manage My Profile
As a driver or passenger, I want to add and update my profile information so that other users can make informed carpooling decisions.

**Acceptance Criteria**:
- A user can add and edit their name, profile photo, and contact details.
- A driver can add vehicle details and available passenger capacity.
- Changes are saved and displayed on the user's profile.

**Priority**: High

### User Story 3: Publish a Ride
As a driver, I want to publish a ride with my route and schedule so that passengers travelling in the same direction can find and request a seat.

**Acceptance Criteria**:
- A driver can enter pickup and destination points, departure date and time, and available seats.
- The system validates required ride details before publishing.
- A published ride appears in relevant passenger search results.

**Priority**: MVP

### User Story 4: Search for Matching Rides
As a passenger, I want to search for rides by pickup, destination, and departure time so that I can find a convenient carpool.

**Acceptance Criteria**:
- A passenger can enter pickup and destination locations and a travel date or time.
- The system displays rides that match the route and schedule criteria.
- Each result shows the driver's profile summary, available seats, departure time, and estimated cost when provided.

**Priority**: MVP

### User Story 5: Receive Route Recommendations
As a driver or passenger, I want the system to recommend users with similar routes and schedules so that I can find suitable carpool matches without searching manually.

**Acceptance Criteria**:
- The system compares route and schedule information from active ride listings and passenger requests.
- Recommendations show the relevant route, time, and match explanation.
- A user can open a recommendation to view its details.

**Priority**: High

### User Story 6: Request or Book a Seat
As a passenger, I want to request an available seat on a ride so that I can reserve a place with a driver.

**Acceptance Criteria**:
- A passenger can submit a booking request for a ride with available capacity.
- The driver can accept or decline the request.
- The passenger can see the request status, and accepted bookings reduce the available seat count.

**Priority**: MVP

### User Story 7: Manage Ride Bookings
As a driver, I want to view and manage incoming booking requests so that I can control who joins my ride.

**Acceptance Criteria**:
- The driver can view pending, accepted, and declined requests for each ride.
- The driver can accept or decline a pending request.
- The system notifies the passenger when the request status changes.

**Priority**: MVP

### User Story 8: Split and Track Ride Costs
As a driver or passenger, I want to see and agree on how ride costs are shared so that everyone understands their contribution before travelling.

**Acceptance Criteria**:
- A driver can provide an estimated total ride cost or per-passenger contribution.
- Passengers can review the proposed contribution before requesting or confirming a seat.
- The confirmed cost-sharing details are visible to the driver and accepted passengers.

**Priority**: High

### User Story 9: Communicate About a Ride
As a driver or passenger, I want to message the other participants in a confirmed or requested ride so that I can coordinate pickup details and updates.

**Acceptance Criteria**:
- A user can send and receive messages within the relevant ride conversation.
- Messages are visible only to authorized participants of that ride.
- The system indicates when a new message is received.

**Priority**: Medium

### User Story 10: Rate and Review a Ride
As a driver or passenger, I want to rate and review the people I travelled with so that the community can build trust through shared experiences.

**Acceptance Criteria**:
- A participant can submit a rating and optional written review after a ride is marked completed.
- Each eligible participant can submit only one review per other participant for that ride.
- Submitted ratings contribute to the user's visible average rating.

**Priority**: High

### User Story 11: Use Safety and Ride-Sharing Controls
As a passenger or driver, I want access to basic safety information and controls so that I can make safer carpooling decisions and report problems.

**Acceptance Criteria**:
- Users can view the profile and vehicle details shared by the driver before confirming a ride.
- Users can report a ride or participant and provide a reason.
- The system records the report for review by an authorized administrator.

**Priority**: MVP

### User Story 12: Organize Carpools for a Company or University
As a company or university coordinator, I want to manage an organization-specific carpool group so that members can find rides with people from the same organization.

**Acceptance Criteria**:
- An authorized coordinator can create or manage an organization group.
- Members can join after completing the configured organization verification process.
- Group members can find ride listings and requests shared within their organization.

**Priority**: Medium
