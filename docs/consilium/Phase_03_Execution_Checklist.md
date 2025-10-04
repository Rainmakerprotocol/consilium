# Phase 3 Execution Checklist
## Discord Infrastructure Setup for Consilium Relay

**Version**: 1.0  
**Date**: 2025-10-04  
**Estimated Time**: 45-60 minutes (first-time setup)  
**Prerequisites**: Discord account, Python 3.11+, project repository cloned

---

## 📚 Educational Overview

### What We're Building
You're setting up the **Discord side** of the Consilium Relay infrastructure:
- **Bot Application**: A container that holds your bot's configuration
- **Bot User**: The actual automated account that will post messages
- **Server & Channel**: Where multi-AI conversations will take place
- **Credentials**: Tokens and IDs needed for the relay to connect

### Why This Phase is Manual
Discord's Developer Portal requires human authentication and CAPTCHA verification. Automating this would be brittle (UI changes frequently) and potentially violate Discord's Terms of Service. This 45-minute investment creates a stable foundation for all future phases.

### Security Mindset
Treat your **bot token** like a password to your bank account. If exposed:
- Anyone can control your bot
- They can read all messages in channels the bot accesses
- They can post content impersonating your bot

**🔒 Golden Rule**: Never commit `.env` to Git. Never share screenshots with visible tokens.

---

## 🎯 Quick Reference: What You'll Capture

| Item | Format | Example | Storage |
|------|--------|---------|---------|
| Bot Token | 50-80 chars with dots | `MTIz...AbC.dQw4w9` | `.env` (CRITICAL) |
| Guild ID | 18-20 digits | `123456789012345678` | `.env` (Low risk) |
| Channel ID | 18-20 digits | `987654321098765432` | `.env` (Low risk) |
| API Key | 32+ chars, csk_ prefix | `csk_1a2b3c...` | `.env` (CRITICAL) |

---

## ✅ Pre-Flight Checklist

Before starting, ensure you have:
- [ ] Discord account with **verified email**
- [ ] Web browser (Chrome/Firefox/Edge recommended)
- [ ] Text editor for editing `.env` file
- [ ] Screenshot tool (for documentation)
- [ ] Project repository on your machine
- [ ] Terminal/command prompt access
- [ ] 45-60 minutes of uninterrupted time

---

## 📋 Phase 3 Execution: 22-Step Process

### 🔧 PREPARATION (Steps 1-2)

---

#### **Step 1: Enable Discord Developer Mode** ⏱️ 2 min

**Why This Matters**: Developer Mode adds "Copy ID" options to Discord's right-click menus, allowing you to capture the 18-digit numeric IDs for servers and channels.

**Action**:
1. Open Discord (desktop app or web browser)
2. Click ⚙️ **User Settings** (gear icon next to your username, bottom-left)
3. Scroll down to **APP SETTINGS** section
4. Click **Advanced** in left sidebar
5. Toggle **Developer Mode** ON (should turn blue)
6. Close settings

**✅ Validation**: 
- Right-click any server icon in left sidebar
- You should see "Copy Server ID" in the context menu
- If missing, restart Discord and try again

**📸 Optional Screenshot**: Settings page showing Developer Mode enabled

**💡 Educational Note**: Discord uses "Snowflake IDs" - unique 18-20 digit numbers for every object (servers, channels, users, messages). These IDs are permanent and used by the API to reference specific resources.

---

#### **Step 2: Navigate to Discord Developer Portal** ⏱️ 1 min

**Why This Matters**: The Developer Portal is Discord's control center for creating and managing bot applications. It's separate from the main Discord app.

**Action**:
1. Open web browser (new tab)
2. Navigate to: `https://discord.com/developers/applications`
3. Log in with your Discord account if prompted
4. Complete 2FA if enabled (recommended for security)

**✅ Validation**: 
- You should see "Applications" page
- Header says "My Applications"
- Blue "New Application" button visible in top-right

**📸 Required Screenshot**: Save as `01_developer_portal.png`
- Show the Applications page with "New Application" button visible
- Redact any email addresses if shown

**💡 Educational Note**: This portal is where developers manage bots, OAuth2 apps, and game integrations. Everything we do here is configuration - no code required yet.

---

### 🤖 BOT CREATION (Steps 3-6)

---

#### **Step 3: Create Discord Application** ⏱️ 2 min

**Why This Matters**: Applications are containers for bots, OAuth2 credentials, and permissions. Think of it as creating a "project" that will house your bot.

**Action**:
1. Click **New Application** button (top-right)
2. Modal appears: "Create an Application"
3. Enter name: `Consilium Relay Bot`
4. ✅ Check: "I agree to the Discord Developer Terms of Service and Developer Policy"
5. Click **Create** button

**✅ Validation**: 
- You're redirected to the application's **General Information** page
- Application name shows "Consilium Relay Bot" at the top
- Left sidebar shows multiple tabs (General Information, Bot, OAuth2, etc.)

**📸 Required Screenshot**: Save as `02_create_application.png`
- Capture the "Create an Application" modal with name filled in
- Or capture the resulting General Information page

**💡 Educational Note**: The application name is what users will see when your bot joins their server. Choose something descriptive and professional. You can change it later if needed.

**🚨 Common Pitfall**: Don't close the browser tab! Keep this portal open throughout setup.

---

#### **Step 4: Add Bot User** ⏱️ 1 min

**Why This Matters**: The Application is just a container. The Bot user is the actual automated account that will connect to Discord's gateway and interact with channels.

**Action**:
1. In left sidebar, click **Bot** tab
2. Click **Add Bot** button
3. Confirmation modal: "Add a bot to this app?"
4. Read the warning (bot creation is permanent)
5. Click **Yes, do it!** button

**✅ Validation**: 
- Bot section now shows bot configuration
- You see a **TOKEN** section (still hidden)
- Bot has a default username (matches application name)
- Bot has a default avatar (Discord logo)

**📸 Required Screenshot**: Save as `03_bot_tab.png`
- Show the Bot tab after bot is created
- Token should still be hidden (not revealed yet)

**💡 Educational Note**: Bots are special Discord accounts that can't log in normally (no email/password). They authenticate using a **token** instead, which you'll copy in the next step.

**⚠️ Important**: Once you add a bot, you cannot remove it without deleting the entire application. This is permanent.

---

#### **Step 5: Copy Bot Token** ⏱️ 2 min

**Why This Matters**: The token is your bot's password. The relay service will use this token to authenticate as the bot and connect to Discord's gateway.

**Action**:
1. In Bot section, locate **TOKEN** field
2. Click **Reset Token** button
3. Confirmation modal: "Are you sure you want to reset your token?"
4. Click **Yes, do it!** to confirm
5. Token is now visible (long string with dots, looks like: `MTIz...GX1.AbC...dQw`)
6. Click **Copy** button next to token
7. **IMMEDIATELY** paste token into a secure location:
   - Password manager (recommended)
   - OR temporarily in a text file you'll delete after `.env` creation

**✅ Validation**: 
- Token is copied to clipboard
- Token length is 50-80 characters
- Token contains dots (`.`) - format: `[base64].[base64].[base64]`

**📸 Required Screenshot**: Save as `04_token_reveal.png`
- **CRITICAL**: Use image editor to place BLACK BAR over the token
- Show the Token section but with token completely hidden
- Add annotation: "⚠️ TOKEN REDACTED - Never Share"

**💡 Educational Note**: The token format has three parts separated by dots:
1. **User ID** (base64 encoded)
2. **Timestamp** (when token was created)
3. **HMAC signature** (cryptographic proof of authenticity)

**🚨 CRITICAL SECURITY WARNING**: 
- Treat this token like your bank password
- Never commit to Git, never share in screenshots, never post in Discord
- If you accidentally expose it, come back to this page and click "Reset Token" immediately
- Old token becomes invalid, new token is generated

**🚨 Common Pitfall**: Token is only shown ONCE. If you close the page without copying, you'll need to reset to see it again.

---

#### **Step 6: Configure Bot Settings** ⏱️ 2 min

**Why This Matters**: These settings control bot visibility and baseline permissions.

**Action**:
1. Still on Bot page, scroll down to find:
   - **PUBLIC BOT** toggle
   - **REQUIRE OAUTH2 CODE GRANT** toggle
2. Turn OFF **PUBLIC BOT** (toggle should be gray/disabled)
   - This prevents others from inviting your bot to their servers
3. Leave **REQUIRE OAUTH2 CODE GRANT** OFF (default)
   - OAuth2 code grant is for user-facing apps, not bots

**✅ Validation**: 
- Public Bot toggle is gray/disabled
- Require OAuth2 Code Grant toggle is gray/disabled

**💡 Educational Note**: 
- **Public Bot ON** = Anyone with invite link can add bot to any server
- **Public Bot OFF** = Only you (bot owner) can invite bot
- For internal/private bots, always keep Public Bot disabled

---

### 🔐 PERMISSIONS & INTENTS (Steps 7-8)

---

#### **Step 7: Enable Message Content Intent** ⏱️ 2 min

**Why This Matters**: By default, bots cannot read message content (privacy protection). Since our relay needs to fetch messages for the `GET /v1/strategy/fetch` endpoint, we must explicitly enable the **Message Content Intent** (a privileged permission).

**What Are Intents?**: Intents are permissions that control what events Discord sends to your bot. Standard intents are always available; privileged intents require explicit enablement and (for bots in 100+ servers) Discord verification.

**Action**:
1. Scroll down on Bot page to **Privileged Gateway Intents** section
2. Find three toggles:
   - PRESENCE INTENT
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT ← **This one!**
3. Click **MESSAGE CONTENT INTENT** toggle to enable (turns blue)
4. Modal may appear: "Enable Message Content Intent?"
5. Read the warning about privileged intent
6. Click **Got it** or **Enable** to confirm
7. Scroll to top of page
8. Click **Save Changes** button (green, top-right)

**✅ Validation**: 
- MESSAGE CONTENT INTENT toggle is blue with checkmark
- Save Changes button shows success message

**📸 Required Screenshot**: Save as `05_intents.png`
- Show Privileged Gateway Intents section
- MESSAGE CONTENT INTENT should be enabled (blue)
- Other two intents should be disabled (gray)

**💡 Educational Note**: 
- **Privileged intents** are high-sensitivity permissions
- For bots in <100 servers: Enable freely in Developer Portal
- For bots in 100+ servers: Must apply for Discord verification
- MVP is single-server, so we're well under the limit

**Required Intents for Consilium**:
- ✅ **MESSAGE CONTENT** (privileged) - Read message text
- ✅ **GUILDS** (standard) - Receive server events
- ✅ **GUILD_MESSAGES** (standard) - Receive message events

**Not Needed**:
- ❌ **PRESENCE** - We don't track who's online
- ❌ **SERVER MEMBERS** - We don't need member updates

---

#### **Step 8: Generate Bot Invite URL** ⏱️ 3 min

**Why This Matters**: To add your bot to a Discord server, you need an OAuth2 invite URL with the correct scopes (what the bot is) and permissions (what the bot can do).

**Action**:
1. In left sidebar, click **OAuth2** tab
2. Click **URL Generator** sub-tab
3. In **SCOPES** section, check: ✅ **bot**
4. **BOT PERMISSIONS** section appears below
5. In **TEXT PERMISSIONS** subsection, check these boxes:
   - ✅ **Send Messages** (required for posting)
   - ✅ **Send Messages in Threads** (required for thread posting)
   - ✅ **Create Public Threads** (required for start-thread endpoint)
   - ✅ **Embed Links** (required for attribution embeds)
   - ✅ **Read Message History** (required for fetch endpoint)
6. Scroll down to **GENERATED URL** section (bottom of page)
7. You'll see a long URL starting with: `https://discord.com/api/oauth2/authorize?client_id=...`
8. Click **Copy** button

**✅ Validation**: 
- URL copied to clipboard
- URL is very long (200+ characters)
- URL contains `scope=bot` and `permissions=` parameters

**📸 Required Screenshot**: Save as `06_oauth_url.png`
- Show URL Generator page with bot scope checked
- Show the 5 required permissions checked
- Can include the generated URL (it's not sensitive)

**💡 Educational Note**: 

**What are Scopes?**
- **bot** scope = "This is a bot account" (vs. user OAuth)
- Other scopes exist for different integration types (webhooks, applications.commands)

**Permission Explanations**:
- **Send Messages**: Bot can post text/embeds in channels (core functionality)
- **Read Message History**: Bot can retrieve past messages (for fetch endpoint)
- **Create Public Threads**: Bot can create discussion threads (for start-thread endpoint)
- **Send Messages in Threads**: Bot can reply in threads it creates
- **Embed Links**: Bot can post rich embeds (used for attribution footers)

**Permissions NOT Granted** (good security practice):
- ❌ **Manage Messages** (deleting/pinning) - Not needed, potential abuse vector
- ❌ **Mention Everyone** (@everyone) - Not needed, annoying
- ❌ **Manage Threads** (archiving, locking) - Handled by API, not bot directly
- ❌ **Administrator** (god mode) - **NEVER grant to bots**

**🔢 Permission Calculation**: 
The `permissions=` number in the URL is a bitfield (sum of permission flags). For our setup, it should be around **274877910016** (send messages + read history + create threads + embed links).

---

### 🏠 SERVER SETUP (Steps 9-11)

---

#### **Step 9: Create or Select Discord Server** ⏱️ 5 min

**Why This Matters**: Your bot needs a Discord server (called a "Guild" in the API) to join. You can either create a new server specifically for Consilium or use an existing one where you have admin permissions.

**Option A: Create New Server** (Recommended for MVP)

**Action**:
1. In Discord app, click **+** icon in server list (left sidebar, at bottom)
2. Click **Create My Own**
3. Select template:
   - **For me and my friends** (simple, minimal setup)
   - OR **For a club or community** (more features, requires Community setup)
4. Enter server name: `Consilium Strategy Sessions` (or your preferred name)
5. Optional: Upload server icon (can skip for MVP)
6. Click **Create**

**✅ Validation**: 
- New server appears in your server list
- You're automatically the server owner (crown icon)
- Default channels exist (#general, #voice)

**Option B: Use Existing Server**

**Action**:
1. In Discord, select an existing server where you have **Manage Server** permission
2. Right-click server icon → **Server Settings** → **Roles**
3. Verify you have a role with "Manage Server" permission (checkmark)

**✅ Validation**: 
- You can access Server Settings
- You have Manage Server permission (can invite bots)

**💡 Educational Note**: 
- **Server = Guild** (in API terms; Discord calls them "servers" in UI)
- Owner has all permissions
- "Manage Server" permission allows inviting bots
- Community servers have extra features (announcements, discovery) but add complexity

**Recommendation for MVP**: Create a dedicated test server. Keeps Consilium isolated, easier to experiment, no risk of disrupting existing communities.

---

#### **Step 10: Create #consilium-architecture Channel** ⏱️ 2 min

**Why This Matters**: The relay needs a specific text channel to create threads in. This channel acts as the "parent" where all strategy discussion threads will live.

**Action**:
1. In your Discord server, find **TEXT CHANNELS** section (left sidebar)
2. Hover over "TEXT CHANNELS" header → **+** icon appears
3. Click **+** icon
4. Modal: "Create Channel"
5. Channel Type: **Text Channel** (default, do not change)
6. Channel Name: `consilium-architecture` (lowercase, hyphens, no spaces)
7. Optional: Channel Topic: `Multi-AI strategy sessions via Consilium Relay`
8. Private Channel: Leave **unchecked** (bot needs to see it)
9. Click **Create Channel**

**✅ Validation**: 
- New channel appears in channel list: `#consilium-architecture`
- You can view the channel (not private)
- Channel is empty (no messages)

**💡 Educational Note**: 
- **Channel naming convention**: Lowercase, hyphen-separated (e.g., `general-chat`, `project-updates`)
- **Why "architecture"?**: Originally meant for architecture decisions; you can name it anything (e.g., `consilium-strategy`, `ai-sessions`)
- **Channel vs Thread**: Channels are permanent containers; threads are temporary discussions within channels

**Alternative Names** (if you prefer):
- `consilium-strategy`
- `consilium-decisions`
- `ai-collaboration`
- `strategy-sessions`

Just remember to use whatever name you choose when capturing the Channel ID later!

---

#### **Step 11: Invite Bot to Server** ⏱️ 2 min

**Why This Matters**: This step actually adds your bot to the Discord server using the OAuth2 URL you generated. The bot will appear in the member list (initially offline until Phase 4).

**Action**:
1. Open a new browser tab
2. Paste the OAuth2 URL you copied in Step 8
3. Press Enter to navigate to the URL
4. Discord authorization page loads: "An external application wants to access your Discord account"
5. Under "ADD BOT TO:", click dropdown and select your Consilium server
6. Scroll down and review permissions (should match what you selected in Step 8)
7. Click **Authorize** button
8. Complete CAPTCHA (check "I'm not a robot")
9. Success page: "Authorized [Bot Name]"

**✅ Validation**: 
- Success message displays
- Browser can be closed (or keep open for next steps)
- Return to Discord server

**📸 Required Screenshot**: Save as `07_server_invite.png`
- Capture the Discord authorization page
- Show server dropdown and permissions list
- Can be taken before clicking Authorize

**💡 Educational Note**: 
- OAuth2 is an industry-standard authorization protocol
- You're granting your bot permission to access your server
- The permissions are "requested" but can be adjusted in server settings later
- Bot appears offline initially (will go online when Phase 4 connects it)

**🚨 Common Pitfall**: 
- **"You lack permissions to add bots to this server"**: You need Manage Server permission
- **Target server not in dropdown**: Either lacking permissions or bot already in server
- **"Invalid OAuth2 URL"**: URL may have been corrupted; regenerate from Step 8

---

### 📝 CAPTURE CREDENTIALS (Steps 12-16)

---

#### **Step 12: Verify Bot in Member List** ⏱️ 1 min

**Why This Matters**: Visual confirmation that the bot was successfully invited.

**Action**:
1. In Discord, go to your Consilium server
2. Look at **right sidebar** (member list)
3. Scroll down to **BOT** section (bots are grouped separately)
4. Find your bot: **Consilium Relay Bot**
5. Note the **offline** status (gray circle) - this is expected!

**✅ Validation**: 
- Bot visible in member list
- Bot has "BOT" tag next to username
- Status shows offline (gray circle)

**📸 Required Screenshot**: Save as `08_member_list.png`
- Show member list with bot visible
- Highlight the bot's name and BOT tag
- Offline status is normal and expected

**💡 Educational Note**: 
- Bots appear offline until they connect to Discord's gateway
- In Phase 4, when we run `src/discord/client.py`, the bot will go online (green circle)
- The gray circle is NOT an error - it's expected behavior

---

#### **Step 13: Verify Bot Permissions in Channel** ⏱️ 2 min

**Why This Matters**: OAuth2 grants server-level permissions, but channels can override them. We need to ensure the bot has the correct permissions specifically in `#consilium-architecture`.

**Action**:
1. In Discord, navigate to `#consilium-architecture` channel
2. Right-click channel name → **Edit Channel**
3. In left sidebar, click **Permissions** tab
4. Locate bot in permissions list:
   - Look for role named **Consilium Relay Bot**
   - OR look for **@everyone** role (bot inherits these permissions)
5. Click on bot's role to expand
6. Verify these permissions show **green checkmarks** (✓):
   - View Channel
   - Send Messages
   - Send Messages in Threads
   - Create Public Threads
   - Embed Links
   - Read Message History
7. If any are red X or neutral (gray), click to enable (turns green)
8. Click **Save Changes** at bottom

**✅ Validation**: 
- All 6 required permissions are green (✓)
- No red X marks on required permissions
- Save Changes button shows success

**📸 Required Screenshot**: Save as `09_channel_permissions.png`
- Show channel permissions view
- Bot role selected
- All required permissions visible with green checkmarks

**💡 Educational Note**: 
- **Permission Hierarchy**: Server → Category → Channel
- Channel permissions override server permissions
- **Best Practice**: Grant minimal permissions at server level, specific permissions at channel level
- This isolation means bot can ONLY interact with #consilium-architecture, not other channels

**🚨 Common Pitfall**: 
- Bot works everywhere EXCEPT one channel: Check channel-specific permission overrides
- Red X on permission: Channel explicitly denies; click to change to green checkmark

---

#### **Step 14: Capture Guild (Server) ID** ⏱️ 1 min

**Why This Matters**: The relay needs to know which Discord server to connect to. Discord identifies servers using 18-20 digit Snowflake IDs.

**Action**:
1. Ensure Developer Mode is enabled (Step 1)
2. In Discord, **right-click your server icon** (in left sidebar)
3. From context menu, click **Copy Server ID**
4. ID copied to clipboard (18-20 digit number)
5. Paste immediately into a temporary text file or notes app
6. Label it: `GUILD_ID: [paste here]`

**✅ Validation**: 
- ID is exactly 18-20 digits long
- ID contains only numbers (0-9)
- No letters, no spaces, no special characters

**Example**: `123456789012345678` (18 digits)

**💡 Educational Note**: 
- **Guild = Server** (API uses "guild" internally)
- **Snowflake ID format**: `<timestamp><worker_id><process_id><increment>`
- Discord generates IDs based on creation time
- IDs are permanent - never change even if server is renamed

**🚨 Common Pitfall**: 
- Copied user ID instead of server ID: User IDs are also 18 digits; make sure you right-clicked the SERVER icon, not a user
- "Copy Server ID" not in menu: Enable Developer Mode (Step 1), restart Discord

---

#### **Step 15: Capture Channel ID** ⏱️ 1 min

**Why This Matters**: The relay needs to know which specific channel to create threads in. Like server IDs, channels have unique Snowflake IDs.

**Action**:
1. In Discord, **right-click `#consilium-architecture` channel name** (in channel list)
2. From context menu, click **Copy Channel ID**
3. ID copied to clipboard (18-20 digit number)
4. Paste immediately into your temporary text file
5. Label it: `CHANNEL_ID: [paste here]`

**✅ Validation**: 
- ID is exactly 18-20 digits long
- ID contains only numbers
- ID is different from Guild ID (from Step 14)

**Example**: `987654321098765432` (18 digits)

**💡 Educational Note**: 
- Every Discord object (servers, channels, users, messages, roles) has a unique Snowflake ID
- IDs are permanent - channels can be renamed but ID never changes
- API always uses IDs, not names (names can be duplicated; IDs cannot)

---

#### **Step 16: Generate Consilium API Key** ⏱️ 2 min

**Why This Matters**: The relay API needs authentication to prevent unauthorized clients from posting messages. This API key is what Claude MCP and ChatGPT Custom GPT will use to authenticate.

**Action**:
1. Open terminal or command prompt
2. Run this command:
   ```bash
   python -c "import secrets; print('csk_' + secrets.token_hex(32))"
   ```
3. API key printed to console (format: `csk_` + 64 hex characters)
4. Copy the entire output (including `csk_` prefix)
5. Paste into your temporary text file
6. Label it: `API_KEY: [paste here]`

**✅ Validation**: 
- Key starts with `csk_` (Consilium Secret Key)
- Total length: 68 characters (4 prefix + 64 hex)
- Contains only: lowercase letters (a-f) and numbers (0-9) after prefix

**Example**: `csk_1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b`

**💡 Educational Note**: 
- **Why generate instead of using Discord token?**: Separation of concerns
  - Bot token = Discord gateway authentication (for bot)
  - API key = Relay API authentication (for clients calling relay)
- **secrets module**: Python's cryptographically secure random generator
- **token_hex(32)**: Generates 32 random bytes, outputs as 64 hex characters
- **`csk_` prefix**: Makes it easy to identify as Consilium key (pattern borrowed from API key conventions)

**Alternative Method** (if Python unavailable):
1. Go to: https://www.random.org/strings/?num=1&len=64&digits=on&loweralpha=on&unique=on&format=plain
2. Copy the 64-character string
3. Manually prefix with `csk_`
4. Final format: `csk_[64 random characters]`

**🔒 Security Note**: 
- This key is as sensitive as the bot token
- Anyone with this key can post to your relay
- Rotate quarterly or if compromised

---

### 📄 CREATE CONFIGURATION (Steps 17-18)

---

#### **Step 17: Populate .env File** ⏱️ 3 min

**Why This Matters**: The `.env` file is where all secrets and configuration live. The relay service loads these values at startup. This file must NEVER be committed to Git.

**Action**:
1. Open terminal/command prompt
2. Navigate to your project root directory:
   ```bash
   cd /path/to/consilium-relay
   ```
3. Copy the template:
   ```bash
   cp .env.example .env
   ```
4. Open `.env` in your preferred text editor:
   ```bash
   # macOS/Linux
   nano .env
   
   # Windows
   notepad .env
   
   # Or use VS Code
   code .env
   ```
5. Replace placeholder values with your actual credentials from Steps 6, 14, 15, 16:
   ```bash
   DISCORD_BOT_TOKEN=<paste bot token from Step 6>
   DISCORD_GUILD_ID=<paste guild ID from Step 14>
   DISCORD_CHANNEL_ID=<paste channel ID from Step 15>
   CONSILIUM_API_KEY=<paste API key from Step 16>
   LOG_LEVEL=INFO
   ```
6. Save the file
7. Close your text editor

**✅ Validation**: 
- `.env` file exists in project root
- All 5 variables have actual values (no "your_token_here" placeholders)
- No extra spaces around `=` signs
- No quotes around values

**Example `.env` (with fake values)**:
```bash
DISCORD_BOT_TOKEN=MTIzNDU2Nzg5MDEyMzQ1Njc4OTAuGX1AbC.dQw4w9WgXcQ_example_token_here_not_real
DISCORD_GUILD_ID=123456789012345678
DISCORD_CHANNEL_ID=987654321098765432
CONSILIUM_API_KEY=csk_1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b
LOG_LEVEL=INFO
```

**💡 Educational Note**: 
- **`.env` file format**: Simple `KEY=VALUE` pairs, one per line
- **No spaces**: `KEY=value` (correct) vs `KEY = value` (incorrect)
- **No quotes needed**: `KEY=value` (correct) vs `KEY="value"` (works but unnecessary)
- **Comments**: Lines starting with `#` are comments (ignored)

**LOG_LEVEL Options**:
- **DEBUG**: Very verbose, shows every detail (for development)
- **INFO**: Standard logging, shows important events (recommended for MVP)
- **WARNING**: Only warnings and errors
- **ERROR**: Only errors and critical failures
- **CRITICAL**: Only critical system failures

**🔒 Security Checklist**:
- [ ] `.env` is in `.gitignore` (verify: `cat .gitignore | grep .env`)
- [ ] `.env` is not staged in Git (verify: `git status` shows nothing)
- [ ] File permissions restrict access: `chmod 600 .env` (Unix/macOS only)

**🚨 Critical**: If you accidentally commit `.env` to Git:
1. Immediately rotate all credentials (bot token, API key)
2. Remove from Git history: `git rm --cached .env`
3. Add to `.gitignore` if not already
4. Force push (or reset) to remove from remote

---

#### **Step 18: Validate .env File** ⏱️ 2 min

**Why This Matters**: Catch configuration errors now before Phase 4 tries to connect. Validation checks format and value lengths without testing actual connectivity.

**Action**:
1. In terminal, from project root, run:
   ```bash
   python - <<'PY'
   import re, pathlib, sys

   print("🔍 Validating .env configuration...")
   
   try:
       env = pathlib.Path(".env").read_text(encoding="utf-8")
       
       def get(k):
           m = re.search(rf'^{k}=(.+)$', env, flags=re.M)
           return m.group(1).strip() if m else None
       
       token = get("DISCORD_BOT_TOKEN")
       guild = get("DISCORD_GUILD_ID")
       channel = get("DISCORD_CHANNEL_ID")
       api = get("CONSILIUM_API_KEY")
       log = get("LOG_LEVEL") or "INFO"
       
       errors = []
       
       # Validate bot token
       if not token:
           errors.append("❌ DISCORD_BOT_TOKEN is missing")
       elif len(token) < 50:
           errors.append(f"❌ DISCORD_BOT_TOKEN too short: {len(token)} chars (need 50+)")
       else:
           print(f"✅ Bot token valid: {len(token)} characters")
       
       # Validate guild ID
       if not guild:
           errors.append("❌ DISCORD_GUILD_ID is missing")
       elif not re.fullmatch(r"\d{18,20}", guild):
           errors.append(f"❌ DISCORD_GUILD_ID invalid format: '{guild}' (need 18-20 digits)")
       else:
           print(f"✅ Guild ID valid: {guild}")
       
       # Validate channel ID
       if not channel:
           errors.append("❌ DISCORD_CHANNEL_ID is missing")
       elif not re.fullmatch(r"\d{18,20}", channel):
           errors.append(f"❌ DISCORD_CHANNEL_ID invalid format: '{channel}' (need 18-20 digits)")
       else:
           print(f"✅ Channel ID valid: {channel}")
       
       # Validate API key
       if not api:
           errors.append("❌ CONSILIUM_API_KEY is missing")
       elif len(api) < 32:
           errors.append(f"❌ CONSILIUM_API_KEY too short: {len(api)} chars (need 32+)")
       else:
           print(f"✅ API key valid: {len(api)} characters")
       
       # Validate log level
       if log not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
           errors.append(f"❌ LOG_LEVEL invalid: '{log}' (must be DEBUG|INFO|WARNING|ERROR|CRITICAL)")
       else:
           print(f"✅ Log level valid: {log}")
       
       if errors:
           print("\n⚠️  VALIDATION FAILED - Fix these errors:\n")
           for e in errors:
               print(f"  {e}")
           sys.exit(1)
       else:
           print("\n🎉 ALL VALIDATION CHECKS PASSED!")
           print("✅ .env file is properly configured")
           print("\n📋 Configuration Summary:")
           print(f"   Bot Token: {len(token)} chars (redacted)")
           print(f"   Guild ID: {guild}")
           print(f"   Channel ID: {channel}")
           print(f"   API Key: {len(api)} chars (redacted)")
           print(f"   Log Level: {log}")
           print("\n✅ Ready for Phase 4: Core Framework")
   
   except FileNotFoundError:
       print("❌ .env file not found!")
       print("Run: cp .env.example .env")
       sys.exit(1)
   except Exception as e:
       print(f"❌ Validation error: {e}")
       sys.exit(1)
   PY
   ```

**✅ Expected Output**:
```
🔍 Validating .env configuration...
✅ Bot token valid: 72 characters
✅ Guild ID valid: 123456789012345678
✅ Channel ID valid: 987654321098765432
✅ API key valid: 68 characters
✅ Log level valid: INFO

🎉 ALL VALIDATION CHECKS PASSED!
✅ .env file is properly configured

📋 Configuration Summary:
   Bot Token: 72 chars (redacted)
   Guild ID: 123456789012345678
   Channel ID: 987654321098765432
   API Key: 68 chars (redacted)
   Log Level: INFO

✅ Ready for Phase 4: Core Framework
```

**💡 Educational Note**: 
- This script validates **format**, not **functionality**
- It checks lengths and patterns but doesn't test Discord connectivity
- Actual connectivity testing happens in Phase 4 when bot connects

**🚨 Common Errors**:

| Error | Cause | Solution |
|-------|-------|----------|
| Token too short | Copied partially | Reset token, copy entire string |
| Guild ID invalid format | Has letters/spaces | Right-click server icon, copy ID |
| Channel ID invalid format | Copied message ID instead | Right-click channel name, copy ID |
| API key too short | Generated incorrectly | Re-run Python command, copy full output |
| LOG_LEVEL invalid | Typo (e.g., "info" not "INFO") | Use uppercase: INFO, DEBUG, etc. |

---

### 📚 DOCUMENTATION (Steps 19-21)

---

#### **Step 19: Create Setup Documentation** ⏱️ 10 min

**Why This Matters**: Documenting your setup process creates a reference for:
- Future troubleshooting
- Team members who need to replicate setup
- Your future self (6 months from now)
- Compliance/audit trail

**Action**:
1. Create file: `docs/04_DISCORD_SETUP.md`
2. Use this template structure:

```markdown
# Discord Setup Guide - Consilium Relay

**Date Completed**: 2025-10-04  
**Completed By**: [Your Name]  
**Estimated Time**: 45 minutes  

---

## Prerequisites Completed

- [x] Discord account with verified email
- [x] Python 3.11+ installed
- [x] Project repository cloned
- [x] Developer Mode enabled

---

## Setup Summary

This document records the Discord infrastructure setup for Consilium Relay MVP.

**Bot Details**:
- Application Name: Consilium Relay Bot
- Bot Username: consilium-relay (or auto-generated)
- Application ID: [Redacted - available in Developer Portal]

**Server Details**:
- Server Name: [Your Server Name]
- Guild ID: [18-digit ID from .env]
- Target Channel: #consilium-architecture
- Channel ID: [18-digit ID from .env]

---

## Part 1: Created Discord Application & Bot

**Steps Completed**:
1. ✅ Navigated to Discord Developer Portal
2. ✅ Created new application: "Consilium Relay Bot"
3. ✅ Added bot user to application
4. ✅ Copied and secured bot token

**Key Configuration**:
- Public Bot: Disabled (private to this server)
- OAuth2 Code Grant: Disabled (not needed for bots)

---

## Part 2: Configured Bot Intents

**Steps Completed**:
1. ✅ Enabled MESSAGE CONTENT INTENT (privileged)
2. ✅ Verified GUILDS intent (standard, auto-enabled)
3. ✅ Verified GUILD_MESSAGES intent (standard, auto-enabled)

**Why Message Content Intent?**:
Required for relay to read message content via GET /v1/strategy/fetch endpoint.

---

## Part 3: Generated Bot Invite Link

**Steps Completed**:
1. ✅ Used OAuth2 URL Generator
2. ✅ Selected 'bot' scope
3. ✅ Configured required permissions:
   - Send Messages
   - Read Message History
   - Create Public Threads
   - Send Messages in Threads
   - Embed Links

**OAuth2 URL**: [Redacted - can be regenerated from Developer Portal]

---

## Part 4: Created/Configured Discord Server

**Option Selected**: [Created new server / Used existing server]

**Server Configuration**:
- Server Name: [Your Choice]
- Created channel: #consilium-architecture
- Channel topic: "Multi-AI strategy sessions via Consilium Relay"

---

## Part 5: Invited Bot to Server

**Steps Completed**:
1. ✅ Opened OAuth2 URL in browser
2. ✅ Selected target server from dropdown
3. ✅ Authorized bot with permissions
4. ✅ Completed CAPTCHA
5. ✅ Verified bot in member list

**Bot Status**: Offline (expected until Phase 4)

---

## Part 6: Captured IDs

**Steps Completed**:
1. ✅ Enabled Developer Mode in Discord settings
2. ✅ Copied Guild (Server) ID: [18-digit ID]
3. ✅ Copied Channel ID: [18-digit ID]

**ID Format Verification**: Both IDs are 18 digits, numeric only

---

## Part 7: Populated .env File

**Steps Completed**:
1. ✅ Copied .env.example to .env
2. ✅ Populated DISCORD_BOT_TOKEN (72 characters)
3. ✅ Populated DISCORD_GUILD_ID (18 digits)
4. ✅ Populated DISCORD_CHANNEL_ID (18 digits)
5. ✅ Generated and populated CONSILIUM_API_KEY (68 characters)
6. ✅ Set LOG_LEVEL=INFO

**Security Verification**:
- ✅ .env is in .gitignore
- ✅ .env not staged in Git (git status clean)
- ✅ File permissions set (chmod 600 .env)

---

## Part 8: Verified Setup

### Automated Validation Results

```
🔍 Validating .env configuration...
✅ Bot token valid: 72 characters
✅ Guild ID valid: [your ID]
✅ Channel ID valid: [your ID]
✅ API key valid: 68 characters
✅ Log level valid: INFO
🎉 ALL VALIDATION CHECKS PASSED!
```

### Setup Verification Checklist

- [x] Bot registered in Developer Portal
- [x] Message Content intent enabled
- [x] Bot invited to server with correct permissions
- [x] Token stored in .env (not committed)
- [x] Guild and Channel IDs captured
- [x] Bot visible in server member list
- [x] Channel permissions verified (Send Messages, Read History, Create Threads)
- [x] .env validation script passes
- [x] .env is gitignored (not staged in Git)

**Status**: ✅ COMPLETE

---

## Troubleshooting Notes

### Issues Encountered (if any)

[Document any issues you faced and how you resolved them]

Example:
- **Issue**: Bot not visible in member list
- **Cause**: Invite failed silently
- **Solution**: Regenerated OAuth2 URL and re-invited bot

---

## Next Steps

**Phase 4: Core Framework**
- Implement FastAPI application
- Connect bot to Discord gateway (bot will go online)
- Test health check endpoint

**Phase 5: API Endpoints**
- Implement POST /v1/strategy/start-thread
- Implement POST /v1/strategy/post
- Implement GET /v1/strategy/fetch

---

## Security Notes

- ⚠️ Bot token and API key are CRITICAL secrets
- 🔒 Never commit .env to version control
- 🔄 Rotate credentials quarterly or if compromised
- 📸 Screenshots contain redacted tokens (black bars)

---

## References

- Discord Developer Documentation: https://discord.com/developers/docs
- Phase 3 Architecture: phase_03_ARCHITECTURE.yaml
- Phase 3 Implementation: phase_03_IMPLEMENTATION.yaml

---

**Setup Completed**: 2025-10-04  
**Next Review**: After Phase 4 testing
```

3. Save file as `docs/04_DISCORD_SETUP.md`

**✅ Validation**: 
- File exists at `docs/04_DISCORD_SETUP.md`
- All checklist items marked `[x]`
- Guild and Channel IDs documented (actual values)

---

#### **Step 20: Organize Screenshots** ⏱️ 5 min

**Why This Matters**: Visual documentation helps with troubleshooting and knowledge transfer. Screenshots serve as "proof of completion" and reference material.

**Action**:
1. Create directory:
   ```bash
   mkdir -p docs/assets/discord_setup
   ```

2. Move/rename your screenshots to:
   - `docs/assets/discord_setup/01_developer_portal.png`
   - `docs/assets/discord_setup/02_create_application.png`
   - `docs/assets/discord_setup/03_bot_tab.png`
   - `docs/assets/discord_setup/04_token_reveal.png` **(Ensure token is REDACTED)**
   - `docs/assets/discord_setup/05_intents.png`
   - `docs/assets/discord_setup/06_oauth_url.png`
   - `docs/assets/discord_setup/07_server_invite.png`
   - `docs/assets/discord_setup/08_member_list.png`
   - `docs/assets/discord_setup/09_channel_permissions.png`

3. Verify all screenshots are present:
   ```bash
   ls -1 docs/assets/discord_setup/
   ```

**✅ Expected Output**:
```
01_developer_portal.png
02_create_application.png
03_bot_tab.png
04_token_reveal.png
05_intents.png
06_oauth_url.png
07_server_invite.png
08_member_list.png
09_channel_permissions.png
```

**🔒 Security**: Before committing screenshots:
- [ ] `04_token_reveal.png` has token completely covered (black bar)
- [ ] No email addresses visible in any screenshot
- [ ] No other sensitive information exposed

---

#### **Step 21: Record Completion** ⏱️ 2 min

**Why This Matters**: Project-level tracking ensures all team members know Phase 3 is complete and Phase 4 can begin.

**Action**:
1. Open or create `PHASE_NOTES.md` in project root
2. Append this entry:

```markdown

---
## Phase 3: Discord Infrastructure Setup

**Status**: COMPLETE  
**Completed**: 2025-10-04T21:00:00Z  
**Executed By**: [Your Name]  
**Duration**: 45 minutes  

### Deliverables Completed
- ✅ Discord bot registered in Developer Portal
- ✅ Message Content intent enabled (privileged)
- ✅ Bot invited to server: [Server Name]
- ✅ .env populated with 5 variables (bot token, guild ID, channel ID, API key, log level)
- ✅ docs/04_DISCORD_SETUP.md created with complete guide
- ✅ 9 screenshots captured and redacted
- ✅ Setup checklist 100% complete

### Validation Results
- ✅ Bot visible in Discord member list (offline status expected)
- ✅ Bot has all required permissions in #consilium-architecture
- ✅ .env validation script passed (all formats valid)
- ✅ .env properly gitignored (not committed)
- ✅ Screenshots redacted (tokens covered)

### Configuration Summary
- **Server**: [Server Name]
- **Guild ID**: [18 digits]
- **Channel**: #consilium-architecture
- **Channel ID**: [18 digits]
- **Bot Token**: 72 chars (secured)
- **API Key**: 68 chars (secured)
- **Log Level**: INFO

### Next Phase
**Phase 4**: Core Framework (Automated - Copilot)
- Implement src/main.py (FastAPI app)
- Implement src/core/config.py (env loader)
- Implement src/core/logging.py (structured logs)
- Mount GET /v1/system/health endpoint
- Bot will connect and go online

**Estimated Time**: 2-3 hours  
**Blockers**: None  
**Issues**: None

### Lessons Learned
- [Any notes about issues encountered or improvements for next time]

---
```

3. Save file

**✅ Validation**: 
- PHASE_NOTES.md contains Phase 3 entry
- Entry marked as COMPLETE
- Date and duration recorded

---

### ✅ FINAL VERIFICATION (Step 22)

---

#### **Step 22: Final Checklist** ⏱️ 5 min

**Why This Matters**: Comprehensive verification before declaring Phase 3 complete and moving to Phase 4.

**Complete Checklist**:

```markdown
## Phase 3 Final Verification Checklist

### Discord Configuration
- [ ] Bot created in Developer Portal
- [ ] Bot token copied and stored securely
- [ ] Message Content intent enabled (blue toggle)
- [ ] Public Bot disabled (gray toggle)
- [ ] OAuth2 URL generated with correct permissions
- [ ] Bot invited to Discord server successfully

### Server & Channel Setup
- [ ] Discord server created or selected
- [ ] #consilium-architecture channel created
- [ ] Bot visible in server member list (offline is OK)
- [ ] Bot has 5 required permissions in channel:
  - [ ] Send Messages
  - [ ] Read Message History
  - [ ] Create Public Threads
  - [ ] Send Messages in Threads
  - [ ] Embed Links

### Credentials Captured
- [ ] Guild (Server) ID copied (18 digits)
- [ ] Channel ID copied (18 digits)
- [ ] API key generated (68 chars with csk_ prefix)
- [ ] All credentials documented in secure location

### .env Configuration
- [ ] .env.example copied to .env
- [ ] DISCORD_BOT_TOKEN populated (50+ chars)
- [ ] DISCORD_GUILD_ID populated (18 digits)
- [ ] DISCORD_CHANNEL_ID populated (18 digits)
- [ ] CONSILIUM_API_KEY populated (32+ chars)
- [ ] LOG_LEVEL set to INFO
- [ ] .env validation script passes

### Security
- [ ] .env is in .gitignore
- [ ] .env not staged in Git (git status clean)
- [ ] Screenshots have sensitive data redacted
- [ ] Credentials stored securely (password manager or .env only)

### Documentation
- [ ] docs/04_DISCORD_SETUP.md created
- [ ] Setup guide contains all 8 parts
- [ ] Setup checklist 100% complete ([x] marks)
- [ ] 9 screenshots captured and organized
- [ ] PHASE_NOTES.md updated with Phase 3 completion

### Validation
- [ ] .env validation script output shows "ALL CHECKS PASSED"
- [ ] Bot visible in Discord (visual confirmation)
- [ ] Channel permissions verified (visual confirmation)
- [ ] Ready for Phase 4 message displayed
```

**Run Final Validation**:
```bash
# Automated checks
python - <<'PY'
import pathlib, re, sys

print("=" * 70)
print("PHASE 3 FINAL VERIFICATION")
print("=" * 70)

checks_passed = 0
checks_total = 0

# Check 1: .env exists
checks_total += 1
if pathlib.Path(".env").exists():
    print("✅ .env file exists")
    checks_passed += 1
else:
    print("❌ .env file missing")

# Check 2: .env has valid content
checks_total += 1
try:
    env = pathlib.Path(".env").read_text(encoding="utf-8")
    def get(k):
        m = re.search(rf'^{k}=(.+)$', env, flags=re.M)
        return m.group(1).strip() if m else None
    
    token = get("DISCORD_BOT_TOKEN")
    guild = get("DISCORD_GUILD_ID")
    channel = get("DISCORD_CHANNEL_ID")
    api = get("CONSILIUM_API_KEY")
    
    if all([token, guild, channel, api]) and len(token) >= 50:
        print("✅ .env contains valid credentials")
        checks_passed += 1
    else:
        print("❌ .env credentials invalid")
except:
    print("❌ .env validation failed")

# Check 3: Setup doc exists
checks_total += 1
if pathlib.Path("docs/04_DISCORD_SETUP.md").exists():
    print("✅ Setup documentation exists")
    checks_passed += 1
else:
    print("❌ Setup documentation missing")

# Check 4: Setup doc has checklist
checks_total += 1
try:
    doc = pathlib.Path("docs/04_DISCORD_SETUP.md").read_text(encoding="utf-8")
    if "[x] Bot registered" in doc and "[x] Message Content intent" in doc:
        print("✅ Setup checklist complete")
        checks_passed += 1
    else:
        print("❌ Setup checklist incomplete")
except:
    print("❌ Setup documentation validation failed")

# Check 5: Screenshot directory exists
checks_total += 1
if pathlib.Path("docs/assets/discord_setup").exists():
    print("✅ Screenshot directory exists")
    checks_passed += 1
else:
    print("❌ Screenshot directory missing")

# Check 6: .env is gitignored
checks_total += 1
try:
    gitignore = pathlib.Path(".gitignore").read_text(encoding="utf-8")
    if ".env" in gitignore:
        print("✅ .env is gitignored")
        checks_passed += 1
    else:
        print("⚠️  .env may not be gitignored")
except:
    print("⚠️  Could not verify .gitignore")

print("=" * 70)
print(f"RESULTS: {checks_passed}/{checks_total} checks passed")
print("=" * 70)

if checks_passed == checks_total:
    print("🎉 PHASE 3 COMPLETE - Ready for Phase 4!")
    print("✅ All automated checks passed")
    print("\n📋 Manual Verification Required:")
    print("   1. Open Discord and verify bot in member list")
    print("   2. Check channel permissions visually")
    print("   3. Confirm screenshots are redacted")
    print("\nOnce manual checks complete, Phase 3 is DONE!")
elif checks_passed >= checks_total - 1:
    print("⚠️  ALMOST COMPLETE - Minor issues found")
    print("Review failures above and address before Phase 4")
else:
    print("❌ PHASE 3 INCOMPLETE - Major issues found")
    print("Review failures above and retry failed steps")
    sys.exit(1)
PY
```

**Expected Output**:
```
======================================================================
PHASE 3 FINAL VERIFICATION
======================================================================
✅ .env file exists
✅ .env contains valid credentials
✅ Setup documentation exists
✅ Setup checklist complete
✅ Screenshot directory exists
✅ .env is gitignored
======================================================================
RESULTS: 6/6 checks passed
======================================================================
🎉 PHASE 3 COMPLETE - Ready for Phase 4!
✅ All automated checks passed

📋 Manual Verification Required:
   1. Open Discord and verify bot in member list
   2. Check channel permissions visually
   3. Confirm screenshots are redacted

Once manual checks complete, Phase 3 is DONE!
```

---

## 🎓 Educational Summary

### What You've Built

You've successfully established the **Discord infrastructure** for Consilium Relay:

1. **Bot Application** - Registered with Discord, configured with proper intents
2. **Bot Account** - Automated user that will post AI messages
3. **Server & Channel** - Communication space for multi-AI discussions
4. **Credentials** - Securely captured and stored locally
5. **Documentation** - Complete setup guide with screenshots

### Key Concepts Learned

| Concept | What It Means | Why It Matters |
|---------|---------------|----------------|
| **Snowflake IDs** | 18-20 digit permanent identifiers | API uses IDs to reference objects precisely |
| **Gateway Intents** | Permission to receive event types | Controls what data Discord sends to your bot |
| **OAuth2 Scopes** | What the application IS | 'bot' scope identifies it as a bot account |
| **Bot Permissions** | What the bot CAN DO | Determines bot's capabilities in channels |
| **Bot Token** | Authentication credential | Allows bot to connect as specific account |
| **.env Files** | Local configuration storage | Keeps secrets out of version control |

### Architecture Overview

```
Discord Developer Portal
         ↓
   [Bot Application]
         ↓
   [Bot Account] ──────token──────→ .env file
         ↓
   Discord Gateway
         ↓
   Your Server
         ↓
   #consilium-architecture
```

The bot is now registered and authorized, but **offline** until Phase 4 connects it.

---

## 🚀 Next Steps: Phase 4 Preview

**Phase 4: Core Framework** (Automated via GitHub Copilot)

You've completed the manual groundwork. Phase 4 builds the relay service:

1. **src/main.py** - FastAPI application entrypoint
2. **src/core/config.py** - Loads .env variables
3. **src/core/logging.py** - Structured JSON logging
4. **GET /v1/system/health** - Health check endpoint

**When Phase 4 runs**: Your bot will connect to Discord and go **online** (green circle).

**Estimated Phase 4 Time**: 2-3 hours (mostly automated)

---

## 📊 Phase 3 Statistics

**Total Steps**: 22  
**Manual Steps**: 22 (100% human, 0% automated)  
**Estimated Duration**: 45-60 minutes  
**Deliverables Created**: 3 files (`.env`, setup guide, PHASE_NOTES entry)  
**Screenshots**: 9 PNG files  
**Security Credentials**: 4 (bot token, guild ID, channel ID, API key)

---

## ✅ Phase 3 Complete!

Congratulations! You've successfully completed Phase 3: Discord Infrastructure Setup.

**Status**: ✅ COMPLETE  
**Next Phase**: Phase 4: Core Framework (Automated)  
**Blocker Status**: None - Ready to proceed

**What Changed**:
- ✅ Discord bot exists and is authorized
- ✅ Server and channel configured
- ✅ Credentials captured and validated
- ✅ Documentation complete

**Bot Status**: Currently offline (expected) - will go online in Phase 4

---

**Questions?** Refer to:
- `docs/04_DISCORD_SETUP.md` (your setup guide)
- `phase_03_ARCHITECTURE.yaml` (technical architecture)
- `phase_03_IMPLEMENTATION.yaml` (detailed procedures)
- Discord Developer Documentation: https://discord.com/developers/docs

---

*Document Version: 1.0*  
*Last Updated: 2025-10-04*  
*Format: Markdown*
