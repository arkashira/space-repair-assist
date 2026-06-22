# Space Repair Assist

A system for requesting and fabricating tools or parts for space repair.

## Usage

1. Create a `ToolOrPart` object with the desired name and description.
2. Create a `SpaceRepairAssist` object.
3. Call `receive_request` to add the `ToolOrPart` object to the request list.
4. Call `process_requests` to fabricate the requested tools or parts.
5. Call `get_fabricated_tools_or_parts` to retrieve the fabricated tools or parts.

## Testing

Run `pytest` to execute the tests.
