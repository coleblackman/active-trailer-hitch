-- This Source Code Form is subject to the terms of the bCDDL, v. 1.1.
-- If a copy of the bCDDL was not distributed with this
-- file, You can obtain one at http://beamng.com/bCDDL-1.1.txt

local M = {}

local ball_43
local ball_42
local cannon_14
local cannon_9

local cooldown
local lastCheckedFireValue -- allows using an input device axis as shooting control, not just on/off buttons

local function onReset()
  electrics.values['mover'] = 0
  electrics.values['mover_input'] = 0
  electrics.values['shoot'] = 0
  cooldown = 0
  lastCheckedFireValue = 0
  for k, node in pairs (v.data.nodes) do
    if node.name == "ball_43" then ball_43=k  end
    if node.name == "ball_42" then ball_42=k  end
    if node.name == "cannon_14" then cannon_14=k  end
    if node.name == "cannon_9" then cannon_9=k  end
  end
end

local function updateGFX(dt) -- ms
  electrics.values['mover'] = math.min(1, math.max(-0.0, (electrics.values['mover'] + electrics.values['mover_input'] * dt * 0.2)))
  if electrics.values['shoot'] == 1 then
    cooldown = cooldown + dt
  end
end

local function fire(VALUE)
  if VALUE < 0.9 then
    -- axis/button is not being pressed down far enough, ignore this event
    lastCheckedFireValue = VALUE
    return
  end
  if lastCheckedFireValue >= 0.9 then return end -- ignore consecutive events after we have passed the 90% threshold: only process the first event of them all
  if VALUE < lastCheckedFireValue then return end -- ignore event if user is in the process of releasing the button/axis (even when above firing threshold)

  lastCheckedFireValue = VALUE
  if electrics.values['shoot'] == 1 then
    -- notify the user *only once* via gui.message
    guihooks.message("Cannon ball was already fired")
    return
  end

  electrics.values['shoot'] = 1 -- trigger actual shooting via thruster

  obj:playSFXOnce("event:>Special>cannon_fire", cannon_9, 1, 1)

  obj:queueGameEngineLua("extensions.hook('onCannonFired'," .. obj:getID() .. ")")
end

local function moveHitch(value)
  electrics.values.mover_input = value
end

-- public interface
M.onInit    = onReset
M.onReset   = onReset
M.updateGFX = updateGFX
M.fire      = fire
M.moveHitch = moveHitch

return M
